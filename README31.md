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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b67f012-3f0d-3ced-967b-32e33b3c2ddb | -7.88087 | -44.86455 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 319f8b2f-1d4f-3027-83dd-8642643b3a92 | -7.3602 | -44.87711 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da2daff5-2350-3c71-a857-6cab9e4d0f74 | -5.84347 | -53.54214 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29df7f55-ba01-30e3-8e6f-6c562fc3f945 | -6.85444 | -43.85729 | 2026-09-20 04:19:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 178fe55b-9803-3e13-9a7b-c78f5eaaa7f4 | -9.28072 | -48.20048 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7688cb44-57ae-385c-a291-0187dc86e29a | -9.68759 | -49.28773 | 2026-09-20 04:19:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6180298-20f6-3ac1-9529-ad42a07c9c43 | -6.92644 | -43.10883 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d86bc352-51c8-3fc2-a2a3-0867e311f029 | -9.25929 | -45.951 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 898fbe97-8930-3675-8583-0e4638469d26 | -9.54374 | -45.39989 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0099e09-cbe8-37d3-b9d5-55a24e3ecf90 | -10.56066 | -46.57279 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f1f0039-9c70-33b8-8f36-c8985db40dab | -6.81929 | -47.88997 | 2026-09-20 04:19:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35b72a72-4f2e-30da-b400-5f8982ab92ab | -9.02741 | -48.72456 | 2026-09-20 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fdab87f3-90af-3e3e-8178-62c3121c1c0b | -6.3143 | -47.63224 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c404929-3da7-3dd7-b66d-604a9d64f124 | -7.16038 | -47.42852 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92959f68-f3c8-3356-8537-8345722b1ba5 | -11.34231 | -43.38633 | 2026-09-20 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1862bb8-24fd-3f57-85a4-f22e420d1b33 | -10.30671 | -50.2681 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7c923cfc-d8ac-3805-8853-7ecb1d85894b | -8.26156 | -50.85884 | 2026-09-20 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0b385a6-af8b-3e26-88c9-680ce519b02d | -5.84722 | -53.56146 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a58234c6-3858-3a3c-bff0-912cd4492a44 | -7.36161 | -44.86877 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3adb81bd-7ec0-34da-a3b4-cae175a383f8 | -5.64021 | -43.37456 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a0011ce-5570-3434-aeef-fe8a7aec5783 | -7.62228 | -45.4548 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c972b463-5c3c-3779-8668-1a5f9bf1eaeb | -8.43931 | -46.86968 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c240e16e-c233-3249-a9ca-bee5ba1194ed | -9.79291 | -45.06495 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aaffb072-66da-3715-a2db-82eb4793b668 | -7.12677 | -42.07592 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a9981ffe-e31e-328d-8771-70e7333731c1 | -9.73168 | -46.08422 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2b11f79-32ee-3e1c-b668-413956e1b560 | -11.28613 | -41.99809 | 2026-09-20 04:19:00 | NPP-375D | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c1bf161d-9150-3974-80e1-1d4b96e6f6b4 | -6.51505 | -47.13523 | 2026-09-20 04:19:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 914e8deb-819e-3dd8-a501-aec0c414cc83 | -5.34824 | -44.83265 | 2026-09-20 04:19:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d665c63f-2a0a-3a22-8b90-637646e970ca | -8.43218 | -46.8633 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d69ad300-5711-3fe1-8dad-5dcddfbfda6e | -9.79646 | -45.06557 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18cb141c-c5af-3bdd-bff4-e00b71dda23b | -8.1831 | -54.7688 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 058c2e38-e763-3586-8e82-86935ba5ee3e | -7.80156 | -44.94079 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7608536c-1bd8-321e-93e3-dc59ed51a65e | -11.41321 | -44.21869 | 2026-09-20 04:19:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55c65b22-e4ca-363c-95c6-94a3348a9473 | -11.012 | -48.31108 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 566219f6-2b70-356d-90b0-c915cb2fa6e4 | -11.03513 | -48.30322 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2aa2bc29-6307-3bcd-b5b1-1f3713ec58ff | -9.01926 | -44.91659 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60a19585-ea2b-3dec-95b1-40deebd4c729 | -7.77103 | -44.83031 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c758fc1-927b-3472-9dc5-e4a6371949db | -10.13596 | -45.56227 | 2026-09-20 04:19:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2369629-f732-3b39-9694-368cd04bc611 | -10.1021 | -48.43216 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4bcf0889-5037-38ac-83d4-304d4f8a36ed | -4.68466 | -46.40277 | 2026-09-20 04:19:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ff0c48ea-f23a-368b-b739-9a259b07a1e2 | -8.07641 | -55.34679 | 2026-09-20 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4153eb5-88ad-366b-b66d-c9f23f6136dc | -10.8378 | -50.93414 | 2026-09-20 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2905ad12-7bfb-367f-a5e0-bf7fc78e8d35 | -7.59297 | -46.97581 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5db11f41-42d6-3e66-a948-445279567adb | -10.48954 | -46.26897 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b9248ba2-0ea7-3457-a686-ad824cfca0cd | -4.8444 | -48.64719 | 2026-09-20 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4eb1014b-241e-36a3-affe-3feea66651ac | -7.45131 | -44.73029 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 68c0353b-5ecb-32b6-9c02-cbf663604ceb | -9.69675 | -48.31874 | 2026-09-20 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 170133fb-1d8d-31bd-953b-82a535e9f06c | -9.67302 | -54.32148 | 2026-09-20 04:19:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 431f0aff-f26d-3433-b108-04c4e17aff5d | -6.97875 | -42.17416 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 038cbb2a-b583-3d86-8542-b1ae2184607e | -6.51213 | -46.77582 | 2026-09-20 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bea7c7b0-eca9-3a7d-988b-ad4d8823b516 | -9.80694 | -48.31554 | 2026-09-20 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 74ba1f9c-cea2-3b97-b1c3-78cf72605d88 | -7.44636 | -44.73794 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c73d481-e4c0-355f-8600-cacc04255d3d | -7.05593 | -47.53483 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f66f81cb-1e2a-36d4-870f-6d7eca90ba9b | -5.84264 | -53.54976 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ae589b5-c53a-351f-8595-9b5b4862d9d4 | -10.29893 | -50.26766 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| e135d62c-6c83-36ac-a781-f855dc81786c | -11.03722 | -48.31585 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64c797f6-4b22-31e4-a7d1-19b46abe65c7 | -6.56091 | -45.58586 | 2026-09-20 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2e4d53f9-865b-3d9c-a1ba-1be7b418083e | -10.30283 | -50.26177 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cc23f49f-2799-33ce-992f-f16f67f422d6 | -7.39632 | -47.77501 | 2026-09-20 04:19:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 287fd41e-efd9-3da6-9e37-e586bd393c49 | -7.54126 | -48.68758 | 2026-09-20 04:19:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d5d7172-a9e5-3638-b6d1-8fc367448719 | -5.85103 | -53.54015 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e52fb132-81bf-340a-b63e-8e01a3448558 | -9.03511 | -49.83683 | 2026-09-20 04:19:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7ffc477b-d2f9-3f19-a09d-9ecc007eac6f | -7.62609 | -46.7575 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d63c47ff-bd30-350d-9ebc-759feb2456d7 | -10.82271 | -50.93124 | 2026-09-20 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f1ce09d-bdee-3b7d-b888-e67c97d203a9 | -9.26183 | -46.21012 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| acc6f58f-04f8-3b84-982b-c5949d6ae793 | -3.4563 | -50.61172 | 2026-09-20 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33416e26-3424-3258-8fd2-9f0346c966ab | -5.84446 | -53.53687 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c182e845-5702-33df-8f35-1b77a4f897a9 | -8.75254 | -48.65215 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d0226f8-1399-3116-8f4d-87cc1a1e6d12 | -11.00928 | -48.32619 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a8780c2-284a-3f91-bf7d-9568326bf100 | -11.44883 | -45.39634 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 282fb0c0-48b3-3902-9c75-7329a860b9cc | -5.40777 | -44.26916 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 525b712d-3479-3f04-a70c-80ce36aace08 | -10.40184 | -48.36257 | 2026-09-20 04:19:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9fbd59a-cf8a-332e-bba6-16dbd2ba5ab5 | -7.42272 | -44.74696 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f0b248e-f296-3bb9-9999-1f0577821ec6 | -8.39306 | -45.6266 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0a9ffbb0-0345-311c-b646-b6682245af21 | -5.85375 | -49.78991 | 2026-09-20 04:19:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41b00783-ed07-3956-b4c1-f15e427b9844 | -7.15554 | -47.45635 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38bcea9f-4bcc-36b9-b65c-8551b8ba4feb | -9.78157 | -45.0672 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9da0cec8-cbe3-3312-ac85-4e92b2eadc3a | -8.78553 | -48.71241 | 2026-09-20 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 014983e3-5d7b-3c4a-82f5-034564eb9a3e | -5.23843 | -49.40464 | 2026-09-20 04:19:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2362f6e8-189b-342f-b185-13ccfb24663f | -9.79223 | -45.06902 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 108895d5-cb8b-3480-a072-f60dfe493c80 | -8.15187 | -54.81186 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e6b80b8-90df-3ffc-a462-22749b4dbfc8 | -10.26541 | -45.48106 | 2026-09-20 04:19:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6365e906-1498-3496-b506-42c0cc03d069 | -9.26303 | -45.95166 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18e18234-82bd-3d47-8ff2-fe2bd772db9d | -6.61149 | -43.75634 | 2026-09-20 04:19:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 69c9b3a7-3202-32fe-86ef-64d186710b47 | -7.55508 | -45.43637 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a7aedf80-b107-34f5-9379-b91adfbcc609 | -4.68055 | -46.40209 | 2026-09-20 04:19:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5a90f6f4-8c81-3701-9cdd-ffab4393190b | -10.30032 | -45.42666 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3aba35dc-307b-3841-98cc-3b9fdbe51298 | -11.0309 | -48.3026 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42fd0b11-108a-3bd7-bd28-4e954060f9b9 | -6.97152 | -42.17659 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 20814817-5fca-3981-b943-08ca7ea4404f | -8.1452 | -54.81037 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 253ebebe-ac1c-39de-8bfa-bc5d1149b90c | -11.47636 | -47.78733 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6e6d14c-4967-309c-9350-17f97dfa1e1c | -7.01657 | -45.23771 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35340226-3700-31b5-b69f-3642b8403663 | -11.66394 | -43.42857 | 2026-09-20 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bfdc2b98-3425-3659-9ff9-8c4f46ad4b99 | -9.25787 | -45.9368 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04a8422d-09e1-32dc-8d70-43941359e728 | -7.51968 | -46.67353 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f09b7c9e-2d5b-3af3-8894-1212f84a9bab | -10.4048 | -48.92929 | 2026-09-20 04:19:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef645d5d-33ed-398f-915c-927705fd234c | -5.22615 | -47.57903 | 2026-09-20 04:19:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 490412dc-29ae-3839-8988-25d7891c8bed | -8.42218 | -45.87022 | 2026-09-20 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74906cb4-3a9e-30e3-ae54-5abd2463bb87 | -7.43519 | -44.69393 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae9e528b-6af5-3fa9-a014-7174f0dda835 | -6.51623 | -46.77647 | 2026-09-20 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README32.md)
