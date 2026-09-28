# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60af1a07-5645-38c4-ab41-ce5ca1fd9373 | -0.50976 | -49.12688 | 2026-09-28 05:08:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6634744-de25-3414-abf6-2ad1150cc89d | -1.76832 | -53.76027 | 2026-09-28 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6521884a-9b05-3c9d-9b01-bf7808f70257 | -0.50602 | -49.1263 | 2026-09-28 05:08:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9a253c5-2920-3548-b132-5b4a7c0c6c5e | -2.76766 | -49.48376 | 2026-09-28 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 74c5851a-2f0c-3635-bdd3-559bb7a78fb4 | -2.44617 | -49.22036 | 2026-09-28 05:08:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a53d2bf8-a5d7-3829-91cd-d33217eb54ea | 1.67798 | -55.94952 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6637fefa-9c1d-3d05-ab3b-1a6090d7e3d6 | -1.61968 | -55.1081 | 2026-09-28 05:08:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 534b2a6a-5cab-3b12-869e-3af73d55bf60 | 1.67938 | -55.95832 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efc7976f-407e-3cae-9ecc-5ca7b220cd4b | -3.81993 | -44.09392 | 2026-09-28 05:08:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ea66d3f-51e6-3f5d-80a4-ccae52577482 | 0.70106 | -51.43081 | 2026-09-28 05:08:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15d04304-87e9-386d-ae76-4bfc06e03e1e | -2.77072 | -49.48888 | 2026-09-28 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c3e941d4-edbe-3830-a6f3-7d3f1b027dfa | 0.88808 | -50.78351 | 2026-09-28 05:08:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a93d57a-bb43-3d59-bec9-639a2ec4c3a3 | -1.92777 | -52.13614 | 2026-09-28 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48f4def8-2230-34ec-80fa-3d410decad78 | -2.07886 | -49.54932 | 2026-09-28 05:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 999ca41f-d05c-3165-992e-8d0ea500f0fd | -2.3773 | -50.40843 | 2026-09-28 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b22dd93-4a68-3075-a080-57cdbbbc3aab | -1.775 | -53.76132 | 2026-09-28 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2987d53b-5980-3d8d-97b0-dcea7ab31d53 | 1.26165 | -50.67327 | 2026-09-28 05:08:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fe0ece6-ea51-3b73-9483-b58aacf014d9 | 1.67534 | -55.94715 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab34cb0d-4446-3d4f-ad95-f7c9c0708b6f | 1.66759 | -55.92138 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 801b91bc-6b9f-316a-a6c8-bb62efbd9ff2 | -3.93818 | -42.55566 | 2026-09-28 05:08:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| d6a0f02a-50d6-39eb-b357-aa648d702180 | -1.0453 | -53.56103 | 2026-09-28 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1bc3881-e3a1-3930-8696-6945bff6f4d3 | -1.85788 | -47.97392 | 2026-09-28 05:08:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a1f7c3f-8841-3155-b08e-d38d68434e99 | -0.75691 | -50.56108 | 2026-09-28 05:08:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbeebd8f-313f-393a-af89-faae4e9b2abd | -2.77213 | -49.47983 | 2026-09-28 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 45c55b82-7f96-3c7e-8a27-64cf639b9e32 | -2.9914 | -49.103 | 2026-09-28 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba57204d-a8a2-33bf-be1d-148aa8340674 | 2.36242 | -50.76717 | 2026-09-28 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bab0726-54d2-340f-8b53-23ed5b8fc32b | -1.05142 | -53.56556 | 2026-09-28 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef35b99e-9ca8-3784-b98f-149c3d20e632 | -3.93922 | -42.54975 | 2026-09-28 05:08:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| a28fb0be-683a-30b9-adfe-413c1f216c2c | -2.14855 | -46.17602 | 2026-09-28 05:08:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 761e477b-d472-337d-ab4c-bc7c778baf08 | -2.44999 | -49.22095 | 2026-09-28 05:08:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fbed3dd-c85a-38dd-ba90-2e2b9ba86cbf | 4.30742 | -60.82255 | 2026-09-28 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6191deb-3b81-36a0-8cc2-e5e01deaf2e9 | 4.3454 | -60.71201 | 2026-09-28 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e15ffc21-db75-3d3c-8eca-2b610e548675 | 1.25823 | -50.67381 | 2026-09-28 05:08:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2043da0b-50a1-327e-b69c-a40923cb4a09 | -1.34412 | -55.47601 | 2026-09-28 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 9be1fb04-6862-3715-a0f2-648a079f070c | 2.36299 | -50.77077 | 2026-09-28 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc7a4c33-e8fa-3c93-b71a-08ca851f2d8c | -2.92868 | -48.75533 | 2026-09-28 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0ec45ad-301d-3b73-9bf1-8c35e25a972d | -2.7759 | -49.48043 | 2026-09-28 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4f100dc-a359-3c98-885e-745faef38f83 | -1.04475 | -53.5645 | 2026-09-28 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f678029-5858-3884-8927-a5a63052912c | -1.23321 | -54.09956 | 2026-09-28 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22adb22b-017c-32bd-9e94-f1814f7dd872 | -1.73749 | -57.17926 | 2026-09-28 05:08:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 24f8f446-b0dd-32cd-80e8-73e0a822e8da | 1.67146 | -55.93253 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10a34b86-e9df-3e9a-8189-fb55ed99f498 | -1.93001 | -52.14371 | 2026-09-28 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 35461061-b360-370a-9744-17d70eb7fce8 | -2.86829 | -49.63048 | 2026-09-28 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08b3dccb-2037-3a4c-80c7-0caeeeba9593 | -2.62618 | -51.71647 | 2026-09-28 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bac55f4-8260-3c4d-b0e4-fca2234dedaa | 1.67028 | -55.93894 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4220dfdf-ff1f-35db-90d7-355d37654fbd | 1.64736 | -55.90048 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f998dfc-9cae-31d1-8f14-15b32612873c | -1.05087 | -53.56903 | 2026-09-28 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ecacbbc-d948-31fb-9b49-cb0cf6c0e037 | -1.22985 | -54.09906 | 2026-09-28 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f641fc75-b53e-3bb2-a24a-720a893d17ab | 2.38575 | -51.02305 | 2026-09-28 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98fc3d43-f8ff-3745-a8f3-d65261b3eac1 | -1.10698 | -54.18886 | 2026-09-28 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a7ecef7-21f3-3427-b2ff-c43bc546a454 | -1.81982 | -55.32042 | 2026-09-28 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 006727bb-4017-3947-aa76-c774c96a3422 | 1.67728 | -55.94513 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdd3373c-4f45-3c2d-be7f-dfe4d0687580 | 4.34332 | -60.7082 | 2026-09-28 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2dcdca3-313a-3661-935b-2cc1d801bcdc | 1.65081 | -55.92228 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3138b30-9aaa-388d-8f31-fc3680fb0d1b | -3.3759 | -44.37072 | 2026-09-28 05:08:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1636e64-8cfa-3c69-804f-4131c9b201c7 | -1.95253 | -48.1163 | 2026-09-28 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7bff27f3-c3ef-3ce4-bf7a-a19c52c5958b | -2.77449 | -49.48947 | 2026-09-28 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a184565-40e4-378e-aab7-cba76844fba3 | -3.93855 | -42.55423 | 2026-09-28 05:08:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 5cc19a03-6d91-35c3-8540-80a05af86f74 | 1.66194 | -55.92054 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a9e3fba-b67a-34ed-ae37-b4f03bbd3183 | 1.6696 | -55.93454 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b4a57f6-e18d-341a-8bda-6facfb2e4efd | -3.36787 | -44.36811 | 2026-09-28 05:08:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c2dabe3-027a-37e5-ae21-cb9d33ca1e54 | -2.92945 | -48.75029 | 2026-09-28 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ce8fdcf-9d28-38f5-bb00-997891a996e3 | -1.75268 | -55.64927 | 2026-09-28 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0b6e279-01b8-3364-8622-0e3d7dc029ae | 1.57897 | -50.91067 | 2026-09-28 05:08:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b90ea87e-5e18-3767-b7d4-757f8b34ebd9 | 1.65452 | -55.9217 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91ff5c12-6555-33b8-a99f-56f57eaad331 | -1.04864 | -53.56156 | 2026-09-28 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a5298e5-7e4c-31da-b7ba-d5c93ac022b7 | -1.86142 | -47.9782 | 2026-09-28 05:08:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd1adbfd-db73-330c-bcca-7de8f96afa06 | -3.81496 | -44.08954 | 2026-09-28 05:08:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b596d5e-227f-3e5d-a6dc-bb24702abec0 | 2.38519 | -51.0195 | 2026-09-28 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 551e0fbb-8cf2-3abc-b8c7-946d7828131d | -1.74055 | -57.18456 | 2026-09-28 05:08:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9f8e97e3-5fa5-3247-be92-fe1930cc899d | 1.15507 | -51.16384 | 2026-09-28 05:08:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09421a03-4037-3f2c-864a-17b5062aeb26 | 1.66635 | -55.92434 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b753821d-ee3c-31ec-ad92-18aee888c1a6 | -1.92721 | -52.13966 | 2026-09-28 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f44d2cd-4830-39a1-b59d-3ae41dde1b24 | 4.3438 | -60.71154 | 2026-09-28 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6acc7d27-5197-34c9-8e56-626060013de1 | -1.04809 | -53.56503 | 2026-09-28 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acef97ee-d9fb-357e-a1b4-4819f5faf97b | 4.3487 | -60.70787 | 2026-09-28 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb233501-d563-3697-81d0-2cb2c8e79950 | -1.23041 | -54.09554 | 2026-09-28 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bdf7f0f4-a08e-35d4-9baf-51cad85e3af3 | -1.79255 | -47.94507 | 2026-09-28 05:08:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d601d0c3-0648-303c-9e66-b358dcc615d6 | 2.3947 | -50.99254 | 2026-09-28 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c0d3fc0-4731-3496-ad52-008438135a56 | -1.14862 | -54.10093 | 2026-09-28 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fad60849-e7f7-35d5-8e11-2753c6493dc2 | -1.86197 | -47.97458 | 2026-09-28 05:08:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3027a93-7be1-35d5-9d09-16b079fd050e | -1.8233 | -55.32098 | 2026-09-28 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 448bf603-e4ea-3189-8c8c-65caf1072597 | -1.75707 | -55.12603 | 2026-09-28 05:08:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8de2c970-980a-33b7-a2da-7c35b39e70f2 | -1.9076 | -52.06792 | 2026-09-28 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0649b89-78f1-3b87-9a35-a1f7c133a98b | 2.39134 | -50.99308 | 2026-09-28 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2964d46-5777-3a61-a040-22b8e8d902b6 | 1.67332 | -55.93397 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7252f13b-653b-37c4-abaa-107e3ebbae9c | -1.77389 | -53.76828 | 2026-09-28 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| afff3294-ff35-36b3-9219-96e319b70001 | -1.347 | -55.48048 | 2026-09-28 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 444b40cb-f9d4-39e8-94f0-85558e8de7ed | -3.3786 | -44.36969 | 2026-09-28 05:08:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7842a00-4c17-3905-a367-c3d4d6eb7865 | 1.25096 | -51.13077 | 2026-09-28 05:08:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a1e8a78-2a4c-3833-928a-731ac618a9f4 | 0.70162 | -51.43435 | 2026-09-28 05:08:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43797dd0-455d-3fa7-8a33-af48597e2bcd | -1.14302 | -54.09279 | 2026-09-28 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bceec95-bfad-3587-b546-2c329ca3a12c | -1.14638 | -54.09333 | 2026-09-28 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e986e32-ea16-3d19-93cd-95957fa14c54 | -1.75101 | -56.02488 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0923228a-41f2-399b-b0bf-a491a0bb153b | -2.76836 | -49.47923 | 2026-09-28 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0f70fd6c-a940-37f3-b223-c2453591d709 | 1.67669 | -55.95595 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23da5339-b56c-37a9-a972-e768bddf9b22 | 1.67216 | -55.93693 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e072a5de-120d-3c78-af59-783768356cd6 | -2.2062 | -48.85632 | 2026-09-28 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c98f0bd-c5e7-3f75-83bf-0f77f07c9a51 | 1.67736 | -55.96037 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26b0ae14-7f23-362e-b98e-5658ead9ea78 | -2.76695 | -49.4883 | 2026-09-28 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README45.md)
