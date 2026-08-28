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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f34c97d-d8d5-392d-8190-7900c514d684 | -6.05927 | -44.88805 | 2026-08-28 18:49:00 | AQUA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 081a5942-a1b3-3202-996b-dc6cb5a5f4c9 | -2.72329 | -47.0564 | 2026-08-28 18:49:00 | AQUA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 208.0 |
| 88350918-0f3a-3816-ad5c-09042cb57c71 | -6.1668 | -53.47583 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 240.3 |
| 2d3e3b24-39fd-38b9-800f-d0998f46616d | -4.17309 | -45.11897 | 2026-08-28 18:49:00 | AQUA_M-T | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4812d15d-a961-383e-a6c2-c0f50b1b0a22 | -3.70323 | -45.26297 | 2026-08-28 18:49:00 | AQUA_M-T | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 490c1215-3f56-3bc0-80a0-005f6844dfc0 | -5.95357 | -44.79687 | 2026-08-28 18:49:00 | AQUA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b772e4a2-15fa-3c77-b97b-de11f8a430c7 | -2.78435 | -44.97307 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 69d22003-296f-31bc-bfc9-344bda7002a0 | -3.9558 | -44.02514 | 2026-08-28 18:49:00 | AQUA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 991073a5-28d6-3692-948d-b79f8925de77 | -3.45463 | -43.36112 | 2026-08-28 18:49:00 | AQUA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 4aef432e-fa82-3b29-b892-4a30c2f19f7a | -3.09805 | -49.22516 | 2026-08-28 18:49:00 | AQUA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9936ea3c-7e48-3b99-b9cd-6e5653661c7e | -2.79252 | -45.58069 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 5ae656ed-2d18-3bba-8d5e-058c5ba2c69c | -6.17864 | -45.9227 | 2026-08-28 18:49:00 | AQUA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 165.8 |
| a7ee6a86-4c8d-3b56-98a2-5c77f65baf14 | -6.30038 | -53.58831 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 9257d93c-df23-3beb-bac9-75f1ac9c8a38 | -2.72199 | -47.04755 | 2026-08-28 18:49:00 | AQUA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 273.4 |
| c6129628-5a8d-30cf-95bb-7cb96a2a3f14 | -5.19392 | -49.34837 | 2026-08-28 18:49:00 | AQUA_M-T | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 56cc9320-3277-3313-9547-111edda92938 | -4.97694 | -56.32287 | 2026-08-28 18:49:00 | AQUA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| a4b676c2-5bd1-39eb-bb93-96c6390266b8 | -3.11445 | -43.47947 | 2026-08-28 18:49:00 | AQUA_M-T | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 98604854-602c-3301-a870-a20c36efd541 | -5.48598 | -45.11978 | 2026-08-28 18:49:00 | AQUA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f9dc1b53-0e1a-36e3-81d4-2b56b296c8f9 | -7.49908 | -55.28471 | 2026-08-28 18:49:00 | AQUA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 243373f9-b434-39b7-b49c-14c38ad2eecb | -2.93586 | -45.01443 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| b9cff7e5-47e8-35bd-a8f4-4078f7d0424a | -5.33046 | -45.12547 | 2026-08-28 18:49:00 | AQUA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 25be4a35-9353-34cd-b5e1-9c126930fa0d | -4.85219 | -45.40017 | 2026-08-28 18:49:00 | AQUA_M-T | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 05c105ad-ba1b-35c0-8e75-e293f0557112 | -3.59744 | -43.01378 | 2026-08-28 18:49:00 | AQUA_M-T | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 690e5fec-a361-3945-8a35-74139a8e938e | -3.2206 | -48.61124 | 2026-08-28 18:49:00 | AQUA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 36966445-121e-3856-9963-8ae796740c65 | -5.32119 | -45.12694 | 2026-08-28 18:49:00 | AQUA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 8bed7fcd-77eb-3c97-94ae-1e3bb8214173 | -6.54091 | -55.27252 | 2026-08-28 18:49:00 | AQUA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 39004305-cf45-321c-b5e5-6f6168c174f4 | -6.53714 | -55.2443 | 2026-08-28 18:49:00 | AQUA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 193.0 |
| 49e85bb3-16e1-37a4-8182-0d3a7ead39c9 | -3.21345 | -49.89192 | 2026-08-28 18:49:00 | AQUA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 514704da-eefd-3668-8418-acd4509c522c | -5.82522 | -49.18435 | 2026-08-28 18:49:00 | AQUA_M-T | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 80638744-4175-3e0a-a229-3f14a5a2d795 | -3.22146 | -48.80322 | 2026-08-28 18:49:00 | AQUA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d23ff65a-f760-34f2-a780-f38461471d68 | -2.7308 | -47.04624 | 2026-08-28 18:49:00 | AQUA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| a3741ee4-d408-374b-877b-60e7e458141e | -4.96672 | -56.00804 | 2026-08-28 18:49:00 | AQUA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 95ffdb9f-0eae-3bad-a22e-27a30ae3de0f | -5.47672 | -45.12118 | 2026-08-28 18:49:00 | AQUA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| b9f7b53a-3301-3fe8-aec2-bcc625e80f9c | -6.17729 | -45.9136 | 2026-08-28 18:49:00 | AQUA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2124962f-404c-3df5-b6fb-0d0884c0a5b7 | -2.54165 | -45.32966 | 2026-08-28 18:49:00 | AQUA_M-T | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 28b4e6f3-499c-322e-8711-9e9e1af8366b | -7.12544 | -56.56274 | 2026-08-28 18:49:00 | AQUA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| c6950aac-6650-3ec6-97df-c5fa96e1cd4d | -3.35979 | -44.22615 | 2026-08-28 18:49:00 | AQUA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 84d88c23-1f5b-300a-aa56-0090cd017695 | -4.91211 | -47.42162 | 2026-08-28 18:49:00 | AQUA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fc9f0a5f-b1c7-3537-8ac2-2458e431ce06 | -5.13721 | -49.93204 | 2026-08-28 18:49:00 | AQUA_M-T | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 27cc6b77-b153-3178-9c75-c8c79597e21f | -4.55946 | -54.92399 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 08f4c30f-9732-34b3-a396-147c7d8298d6 | -6.37368 | -54.94844 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 3e07cbd6-cb16-3ca0-9f97-e3d901e68158 | -5.48744 | -45.12949 | 2026-08-28 18:49:00 | AQUA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b7df6ffc-05dc-359a-8bc6-b30c8d68e3a3 | -3.17142 | -49.16147 | 2026-08-28 18:49:00 | AQUA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9cb952f8-f580-313b-8630-25fe2f87c863 | -5.80642 | -52.31907 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| a51d8020-7ead-3bed-9a5a-4fa0310328da | -6.37736 | -54.97485 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| aa189e2e-ae76-3819-9847-73c8630222d4 | -6.3801 | -45.84624 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 62571b5f-8203-39f3-84ff-ddc8ffc17d04 | -4.55617 | -54.90011 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| c3cfdcce-0ecf-3e43-9545-12e5fc424389 | -6.37911 | -54.96991 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| caa4fb6e-fe22-36c1-80bb-e5a8f496efbe | -2.90379 | -43.52385 | 2026-08-28 18:49:00 | AQUA_M-T | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6c275c1f-6b96-34be-a891-63ea938cd25b | -2.54009 | -45.31928 | 2026-08-28 18:49:00 | AQUA_M-T | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| a2771b63-80e7-3a49-8ec1-e2b0c0c8556c | -5.10555 | -43.75508 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 60d14501-f602-32d4-a582-2e53614f72e9 | -2.80765 | -42.82225 | 2026-08-28 18:49:00 | AQUA_M-T | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 772e1c80-d11d-3526-9dbc-ca9b7566ee3d | -5.26197 | -50.96352 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 3d49ad4d-f90b-369b-aea6-8340c0b49ada | -5.22296 | -52.0201 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 27ed97ca-4c6a-3f1f-a7a0-47b76ff77bf8 | -5.61426 | -44.00396 | 2026-08-28 18:49:00 | AQUA_M-T | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d08dc034-dd92-36ad-85b4-1ca6fb9bcea6 | -4.97777 | -56.29752 | 2026-08-28 18:49:00 | AQUA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 5d1386ab-4219-3b74-bec5-856f32af13a7 | -5.57891 | -42.69932 | 2026-08-28 18:49:00 | AQUA_M-T | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 4edaaa7f-6876-3153-a41c-c97a0749c3dd | -6.16961 | -53.49566 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| fadf3b64-fb1e-30d9-8083-3a7eadef012f | -4.79397 | -46.12228 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ed419f01-0c0e-37a7-a8c6-d31d4133968a | -6.57872 | -55.4412 | 2026-08-28 18:49:00 | AQUA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 9d7095dd-9253-3261-8396-562d8ddc7b52 | -4.98226 | -56.32978 | 2026-08-28 18:49:00 | AQUA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 73aad345-83e2-3754-9a24-23ae8e852ebf | -4.79532 | -46.13134 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7a0cce69-2f0f-3af0-b80b-faf5b5064b28 | -5.29102 | -50.94688 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 85057788-e586-3e73-b72d-2be9bd1f401a | -3.71108 | -45.25143 | 2026-08-28 18:49:00 | AQUA_M-T | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| dfb9981b-e8c1-3370-a880-c92c8c23d464 | -7.13089 | -56.55761 | 2026-08-28 18:49:00 | AQUA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 8bfa0456-e1ba-33e1-9f18-f005d20c08d3 | -3.3184 | -48.83854 | 2026-08-28 18:49:00 | AQUA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 96141517-ab99-307f-a56a-d04e3aa9250b | -6.8973 | -51.08182 | 2026-08-28 18:49:00 | AQUA_M-T | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| f06b1a27-56b7-3468-9b7f-1dff23cce82f | -5.28929 | -50.93465 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| e484ab97-ae72-33d2-a266-48b296726450 | -5.13869 | -49.94249 | 2026-08-28 18:49:00 | AQUA_M-T | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| ca3b4c8f-b412-312a-8a2d-ee6c0e79d25e | -5.11571 | -43.75362 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| b3d0d7c8-64a1-3e8d-b26d-bf6a9a8d7c87 | -2.72068 | -47.0387 | 2026-08-28 18:49:00 | AQUA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 21dcb1c2-0a6d-3a80-9022-223026427492 | -2.62721 | -43.73295 | 2026-08-28 18:49:00 | AQUA_M-T | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 85089ecb-0f87-313a-beab-5eda031bd3d0 | -5.94422 | -44.7984 | 2026-08-28 18:49:00 | AQUA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ad533719-5d9f-3d8d-a147-0edc869be951 | -4.843 | -45.40157 | 2026-08-28 18:49:00 | AQUA_M-T | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b0b775d6-4ebb-3f9a-85c8-67d865654a0f | -5.8179 | -52.31726 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| f02328ef-88eb-33c1-a30c-a56230fffe21 | -3.42449 | -43.37957 | 2026-08-28 18:49:00 | AQUA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| afff93c7-f486-3322-a3ea-1aac833680bf | -5.25503 | -50.96987 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 3825f5dd-ef7e-3cb7-8747-b02c8cce1c12 | -6.16895 | -53.49077 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 177.6 |
| 9f350e01-a2d5-38a3-9a07-834a7d3f7f08 | -3.9576 | -44.03722 | 2026-08-28 18:49:00 | AQUA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 42ce62a2-c35f-3664-834c-f988b6bfefd7 | -6.17998 | -45.93171 | 2026-08-28 18:49:00 | AQUA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| faf8f346-d05b-3ea5-b275-e5ceafe8855a | -5.05236 | -51.94792 | 2026-08-28 18:49:00 | AQUA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| fbef53cd-ffd7-3466-ab75-774578723f9d | -3.66146 | -48.97399 | 2026-08-28 18:49:00 | AQUA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1833bce9-24e5-305b-9e6d-ac4110882998 | -7.36257 | -55.16661 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 772f8a3d-ad6d-3941-9198-5a1cf935404c | -2.78274 | -44.96226 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 063314c0-36d3-3164-88cb-c33710159143 | -3.66011 | -48.96482 | 2026-08-28 18:49:00 | AQUA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| a7b736bd-ebc0-34e8-ae17-7e2a3ce11d66 | -5.14825 | -49.94117 | 2026-08-28 18:49:00 | AQUA_M-T | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dc733310-0cc1-30cd-a987-db8fff938e42 | -2.99352 | -48.9569 | 2026-08-28 18:49:00 | AQUA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 07749c64-117d-366a-8dca-4ed37764f121 | -3.2219 | -48.62016 | 2026-08-28 18:49:00 | AQUA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| cd331ad0-6ef4-354f-81a5-80a32312a1fe | -5.93838 | -52.36952 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 19492cb7-8843-3ba6-8fcf-9382c080a555 | -5.81472 | -52.31268 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 059ae81b-84f1-3331-b713-cdc4d96b528d | -6.1663 | -53.47087 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 154.7 |
| 1723a1f3-98fc-340a-a1a1-ce5b519fa8c2 | -4.17156 | -45.10881 | 2026-08-28 18:49:00 | AQUA_M-T | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e0d0e9c6-d47e-376b-baf8-a4c45d9249c7 | -4.33641 | -48.72321 | 2026-08-28 18:49:00 | AQUA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f30759d0-365b-3b3d-a570-1ca555836292 | -2.63055 | -43.7258 | 2026-08-28 18:49:00 | AQUA_M-T | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| d72b93ed-b291-3604-9530-5cba54217e48 | -5.82473 | -52.36489 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| e2ef2e32-aff7-35c2-97d5-fba87d2fbdcf | -6.04452 | -44.0559 | 2026-08-28 18:49:00 | AQUA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 990b7083-5abf-3c5a-bb70-541ebe173516 | -4.97264 | -56.29014 | 2026-08-28 18:49:00 | AQUA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| eea0c03e-2c84-3398-8191-0696cc08a49b | -4.91716 | -43.47687 | 2026-08-28 18:49:00 | AQUA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9e2be7b0-ce3a-320d-b894-118555a15b34 | -5.34187 | -45.15847 | 2026-08-28 18:49:00 | AQUA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| a911b1ea-5cb7-3ed3-a90b-d207497ed0f6 | -3.3616 | -44.23792 | 2026-08-28 18:49:00 | AQUA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |


[Clique aqui para ver as próximas entradas](README166.md)
