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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14d7bdae-57f7-33c9-8b0e-1fe229065678 | -10.63223 | -45.19016 | 2024-10-02 04:46:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9f8b9b2-ed8a-3f61-b727-92da5fc97178 | -10.42169 | -45.27338 | 2024-10-02 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca17f622-6465-3022-8eae-602244cb2e0a | -10.41928 | -45.27119 | 2024-10-02 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be8f190b-88b8-3af4-bfa3-bd778504cf1a | -10.71128 | -46.17751 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c78aae16-46b9-324d-b3e4-903117c6cda9 | -10.70879 | -46.16449 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a3f01c6-c894-3c83-a3d1-6813c7277e5d | -10.7082 | -46.16869 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3b28a05-2873-341e-92f1-cbbc2f8f1166 | -10.70455 | -46.16392 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26fb7fab-f450-3348-a208-0d2713651eaf | -7.84994 | -44.81313 | 2024-10-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7206a25-4983-35dd-ab5a-f085daf2527d | -7.26873 | -43.8197 | 2024-10-02 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 334250a8-7ffa-3a03-a38a-d6d700c20e27 | -7.15967 | -44.22216 | 2024-10-02 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bf8267b3-f94d-38a8-a37d-99f175ccf0ce | -7.15896 | -44.22725 | 2024-10-02 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4430a6ce-c533-3e37-bf80-8ea2e83817f5 | -6.87828 | -44.09195 | 2024-10-02 04:46:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 03b27249-3840-3327-8df4-05f4ab5b253e | -6.873 | -44.096 | 2024-10-02 04:46:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 295dee54-ccf6-3250-a0dc-ea139086134c | -6.86842 | -44.09522 | 2024-10-02 04:46:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a79362da-82a2-3bca-99a8-5f88febe3cad | -9.92248 | -44.08183 | 2024-10-02 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e5cbff3-05fc-3377-bd31-573da4c76107 | -4.9444 | -43.68287 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86f740d1-2d0d-389b-b7fb-3d56087db103 | -5.88126 | -43.72505 | 2024-10-02 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2123fe53-de49-362f-b1ca-b4ae2f8e4e50 | -5.85056 | -43.74023 | 2024-10-02 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6e889f7-5d6b-309c-a50f-621c23bbce61 | -5.83846 | -43.95372 | 2024-10-02 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4b70f1b-6fb2-304f-85ed-325113a30173 | -5.7142 | -43.93707 | 2024-10-02 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 161c07a4-237f-32eb-b3d1-072d253f3d18 | -11.28965 | -46.88286 | 2024-10-02 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05cc0926-472e-3372-bb8a-142cfbe40a9f | -7.07456 | -39.14891 | 2024-10-02 04:46:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1a9b152b-58be-3757-a2a9-fbd9ac139877 | -7.07392 | -39.15392 | 2024-10-02 04:46:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2b1f75ff-57fc-37bc-97ed-0ae36369e068 | -12.14397 | -40.90065 | 2024-10-02 04:46:00 | NOAA-21 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8969f092-b30c-34ef-aad3-d59676fe9117 | -12.14367 | -40.90023 | 2024-10-02 04:46:00 | NOAA-21 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8a76b7fb-7fb0-3ecf-812a-d340ce98ef66 | -5.65522 | -41.25763 | 2024-10-02 04:46:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 858c583b-91fc-35c7-ae7c-40527b774585 | -11.56192 | -42.18517 | 2024-10-02 04:46:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 90588868-b14c-30a8-8f05-c64045b25caa | -11.56044 | -42.18438 | 2024-10-02 04:46:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0a9bddf1-aeed-3106-ba0e-86095dc86971 | -6.21562 | -43.2043 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 839b864b-db88-3c5e-8e2f-48bca61e9a6f | -6.21077 | -43.20359 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| edf2860f-78ef-337a-84fd-646d7be259e6 | -6.16099 | -42.89819 | 2024-10-02 04:46:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 9044e67f-747d-3a50-a258-80fa0e20dbf8 | -6.16012 | -42.90438 | 2024-10-02 04:46:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b7850e20-ccd5-3445-8456-3583d23f1c4a | -6.15455 | -42.90813 | 2024-10-02 04:46:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5098010b-e3de-362b-b929-ef48ee69a593 | -6.15383 | -42.91323 | 2024-10-02 04:46:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d2842cf2-a4d7-3183-9d71-3b29769381e8 | -6.14967 | -42.90689 | 2024-10-02 04:46:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9208d44a-4397-318b-abf9-e78eb9d1a088 | -6.14893 | -42.91217 | 2024-10-02 04:46:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 848b93f6-f868-3eaf-b304-2d4f75c4909a | -5.95734 | -43.26694 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 66d69a16-6e37-30dc-bd33-2e7aa1493659 | -6.30521 | -43.02922 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| afb5b854-ccc0-390b-b4d0-e6a98ccf4bd4 | -6.18911 | -43.42876 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2b217aa-a143-3c39-bbc2-772b4e1523c3 | -5.96906 | -43.4281 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d1f1bb3-dfc1-3d26-8e7d-18a50866cbc4 | -5.96358 | -43.43259 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95ed2c3a-e408-3957-ad13-eedba9153027 | -5.87664 | -43.42384 | 2024-10-02 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 751cc2aa-0a15-35c6-ac5b-8c71cbb1ccd6 | -5.87187 | -43.42325 | 2024-10-02 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f19c41b-70f6-36ee-a060-c0fdeacb83af | -5.8664 | -43.42766 | 2024-10-02 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af262f03-495f-3c8e-986c-97868da0633d | -7.65005 | -42.44851 | 2024-10-02 04:46:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fcc5b49c-d701-35c7-9ec3-e7a928ac7209 | -7.64399 | -42.45395 | 2024-10-02 04:46:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4f1f7453-5c71-3f47-b377-f080e0299ea3 | -7.63879 | -42.45306 | 2024-10-02 04:46:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d749b4fe-e701-398a-8789-8b942a8dc611 | -7.63445 | -42.44588 | 2024-10-02 04:46:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2e3cebce-4d7b-3456-9c76-50ce0cc76dd7 | -7.63402 | -42.44905 | 2024-10-02 04:46:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dbf90531-d9be-3d1c-8021-90b822820b79 | -7.63359 | -42.45223 | 2024-10-02 04:46:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 43ac7277-bbc9-3c32-b199-a1bc1269b9c1 | -7.45312 | -42.51252 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 574c0ba8-f659-3df9-919a-603aedbaa9cd | -7.45269 | -42.51558 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ca2db31f-aab7-39ba-a3a7-e9de8eaf1ff4 | -7.29106 | -42.25182 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1a29ab58-b99e-3a39-93b8-3053b5151cc6 | -7.29097 | -42.25248 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f7d96f80-7a34-3d1b-84ee-b28c9062f604 | -7.2906 | -42.25508 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 52c8b03a-cdca-33a9-8147-47e242526065 | -7.29054 | -42.25574 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8fd63a52-aff5-3a12-b50e-773840007cbe | -7.29015 | -42.25829 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9e644dd9-4df0-3046-9d1c-2ec0af21688c | -7.29011 | -42.25895 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 42c6b943-c4b7-3c7e-bc50-74f3cd595171 | -7.27578 | -42.24603 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 44c34599-6172-389c-bef1-1a2500762e30 | -7.27533 | -42.24925 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cc6ae8e0-209a-30e6-bff4-f64108e606df | -7.27009 | -42.24837 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7d77ed0a-5599-3aa1-a7fb-a6cb4b211ce3 | -6.95682 | -42.50306 | 2024-10-02 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| abcf0154-e843-353f-a05d-0020c577b441 | -6.95641 | -42.50608 | 2024-10-02 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f94837c0-916e-37cb-81b8-4e947a1f13d1 | -6.95127 | -42.50526 | 2024-10-02 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9a1c143f-9d02-38dc-817b-40e1b450e87e | -6.63563 | -42.10623 | 2024-10-02 04:46:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5aa9b701-c343-325c-a12a-d38bdb4de35a | -6.63515 | -42.10962 | 2024-10-02 04:46:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| df82782d-9927-32e6-83c1-cd710a49795e | -7.87092 | -42.671 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f21c0f5c-8110-3c91-b83c-c2b90d161c4c | -7.85489 | -43.07963 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dab7376e-8a69-327e-bf9c-11e9e1ef21c0 | -7.8545 | -43.08249 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6ad06477-41ed-3d81-93b0-0f18f3ee979e | -7.84987 | -43.07896 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6bce74f8-7b26-3833-9709-d4c843accd00 | -7.84486 | -43.07824 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1d7d18ba-ef14-3c85-891e-ba602a042dd7 | -7.83833 | -43.08879 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d6ca2b84-a9f6-3cf9-b41c-a9c6826263d3 | -7.83446 | -43.07959 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fdaf6e9f-e6c2-39d3-859a-46520dbfd76b | -7.83333 | -43.08802 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a62eb760-752e-3a0d-8e95-0a1b469edcbb | -7.83295 | -43.09082 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| da68bb65-23ae-3c99-914c-d03e38796e8e | -7.83258 | -43.09361 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8416f2d0-6665-3dc6-bb82-dd3533a17984 | -7.82944 | -43.0789 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e64cde3c-32b3-3b6d-bdb8-a186b72a2f61 | -7.82907 | -43.0817 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2b088cfb-976f-3092-bc0d-b9f9881782a7 | -7.82869 | -43.08449 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b45cfab0-169a-33d1-ba27-28ee4ca5a9b9 | -7.82832 | -43.08727 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3acf2ef2-3706-3f44-9292-ea58d55694d4 | -7.82795 | -43.09002 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 489a0e00-6ea8-3c37-bf55-e7a91a44ef08 | -7.82722 | -43.09552 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cefa3b8f-c2ad-31a5-b775-5dc4b240d75c | -7.82369 | -43.0837 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0b557915-0a5e-39ac-b3c7-c343a39c7ee9 | -7.82363 | -43.08235 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 25ffe235-d6ad-3c04-9294-96ad96cc8ebb | -7.82324 | -43.0851 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e7c22296-27a5-3bee-b0fe-91a17017409f | -7.76167 | -43.05002 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 38c9df7b-2336-3ac4-8027-a4fd05233044 | -7.76128 | -43.05291 | 2024-10-02 04:46:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d1d33eb1-02cc-3a2d-9bd1-06fc7892adf9 | -7.70862 | -42.991 | 2024-10-02 04:46:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 99c211e7-75c8-3e82-811b-b33d65d2dd26 | -7.7082 | -42.99401 | 2024-10-02 04:46:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 1f3f1578-beee-333e-b3d9-08ff87819b2d | -7.70779 | -42.99697 | 2024-10-02 04:46:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 02a97bd5-df8b-3440-9ceb-69d6e35f8a8d | -7.70317 | -42.99331 | 2024-10-02 04:46:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 5536935e-722c-3eb5-ae21-c728626e7d92 | -7.70277 | -42.9962 | 2024-10-02 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| a9fde6ee-0b96-3c26-9973-e4669a5c82bc | -7.03621 | -42.8221 | 2024-10-02 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7a5a991c-ec3a-3356-97d2-a8600dcec433 | -6.98947 | -42.90174 | 2024-10-02 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ae58892a-1931-329f-a1e0-c192fd1870d1 | -6.98919 | -42.9019 | 2024-10-02 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4f057a0d-4808-3b63-9b6b-09cef4e4e757 | -6.94139 | -43.40058 | 2024-10-02 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e623c950-d571-3672-a98a-f1498793bf1a | -7.32843 | -43.32915 | 2024-10-02 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f53abf1-f138-3fdc-b0d6-a09e11c1705a | -7.32765 | -43.33467 | 2024-10-02 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b51b7bc-9e4b-3482-bd02-a4f9e5d9d720 | -6.94067 | -43.40578 | 2024-10-02 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dcedfd5f-9256-38c1-b059-ca81a1e888b7 | -6.93512 | -43.41029 | 2024-10-02 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README85.md)
