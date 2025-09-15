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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5083ad24-0e2b-33f0-af7d-18cc41303cf6 | -3.75154 | -51.80763 | 2025-09-15 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37dc863e-640a-39e9-9193-0e3a9d7ca184 | -4.17343 | -48.57497 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 623bd794-33cb-3f48-9fbf-9e0679f02917 | -5.47847 | -44.69357 | 2025-09-15 05:08:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a54b08c9-0f1f-3db1-8299-bcfeb9a0ff26 | -3.22161 | -47.63433 | 2025-09-15 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a68109a-c625-3320-9820-104a99a04883 | -3.3845 | -50.28 | 2025-09-15 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd20bcdd-6abc-33f6-9e81-96e1c38684e8 | 4.30928 | -60.96425 | 2025-09-15 05:08:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d4f00a3-2fa5-3fce-8d44-a0e3af3023c2 | -1.89039 | -54.61592 | 2025-09-15 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 431bf9a4-9cfe-3aab-9db0-af6b39db0d80 | -3.38408 | -50.27872 | 2025-09-15 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dfc3618-3fdf-32d0-813d-94f0fd340813 | -3.64876 | -54.05679 | 2025-09-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 08b2dbb2-a653-32dc-8d88-0efebb43e971 | -3.7334 | -55.94382 | 2025-09-15 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70384c27-5bfd-30d7-a179-d6299ba0a20c | -5.33248 | -45.8047 | 2025-09-15 05:08:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bab2f23-34a5-3b31-958e-3bb2773c476b | 4.3099 | -60.96833 | 2025-09-15 05:08:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10aefeba-a56f-3904-88c7-a9f647f5764f | -4.17804 | -48.57878 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cdc7a9b0-cdc0-3e5f-a8db-98360ed2540e | -3.5935 | -47.5192 | 2025-09-15 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f39e40e-0e8d-34f9-af8c-f6ff32aae76e | -4.17386 | -48.572 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7d53483a-8986-3963-8f25-3ab33694dc9a | -3.52844 | -52.86701 | 2025-09-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7659e2f0-fad6-3e83-8c5c-73d885edf23f | -2.95372 | -51.2818 | 2025-09-15 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56a509a4-cf96-3aab-9605-0df0c076a544 | -5.28542 | -45.25992 | 2025-09-15 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d893a5d6-8aaf-3f67-8cc2-3d361b4abc39 | -1.22784 | -54.12453 | 2025-09-15 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6802234d-040b-36b6-ba9b-40059e6778af | -5.3385 | -45.80418 | 2025-09-15 05:08:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c1c3dff-2ef9-3f27-8e85-4538acc9b971 | -3.85702 | -51.33572 | 2025-09-15 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c27bf6b8-ab10-3695-8c8b-a1dec842f783 | -3.79623 | -52.1733 | 2025-09-15 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0edaf01e-13ef-3330-a4d2-3c71ad00a251 | -3.4862 | -52.81183 | 2025-09-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d8c54fe-ce78-3e60-ab4a-54b7a6eaa54a | -4.17888 | -48.5729 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 26e31b30-a0fb-3074-9a27-916dccce6ccc | -4.13344 | -48.819 | 2025-09-15 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1166f989-30eb-3039-843b-860ff57d5f16 | -3.59632 | -47.52056 | 2025-09-15 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c980d40-fe9d-3a88-89fe-ef65e2cecd46 | -3.64938 | -54.0528 | 2025-09-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84cd3043-9698-3085-a262-f3a29843f7ec | -5.47718 | -44.6899 | 2025-09-15 05:08:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ba46242-a4d0-3bda-a4ea-0f60bb03fb40 | -5.33237 | -45.80303 | 2025-09-15 05:08:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b1c491f-08ec-3346-8bf2-992c25b60f23 | -4.13268 | -48.81767 | 2025-09-15 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28ef49b7-25ec-3244-b066-94fda0a1e1db | -3.59731 | -47.51376 | 2025-09-15 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d918dc84-5769-342e-80bf-8ce63c5fa4c4 | -4.18001 | -48.57208 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a3104e4f-40f9-3d0d-ba4a-3c3bd24999fa | -3.55956 | -53.52896 | 2025-09-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5c7e71a-6b52-344c-8d81-df3c7b4d1ead | -3.51479 | -52.75123 | 2025-09-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a84e4f1b-0e41-3991-9b2a-1d215398eee8 | -1.23824 | -54.10314 | 2025-09-15 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 364f2fa4-50f8-389d-af90-8515563da093 | -2.26175 | -47.84618 | 2025-09-15 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee5cc8f2-479c-3801-8580-fc46cd3927d3 | -3.35515 | -51.59618 | 2025-09-15 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8382c652-708a-39c0-849e-9190bc7a839d | -2.94624 | -49.3483 | 2025-09-15 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25e56b7f-b581-3b66-b0ea-003afe76fdb8 | -2.12123 | -56.86438 | 2025-09-15 05:08:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6142ee5a-664d-3c99-a35c-a40a473e6a19 | -5.47268 | -44.68681 | 2025-09-15 05:08:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ba0adbd-5153-30d6-85ed-e2749249bd8d | -5.11727 | -46.13248 | 2025-09-15 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1df9db4e-62c1-3ef4-b12a-296a40c8ccad | -4.17454 | -48.57415 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d442ccb-5443-3777-8b0b-07ec863e52ca | -2.81045 | -48.62617 | 2025-09-15 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9725d06f-6d5e-3f44-a27b-934696a0d630 | -3.64649 | -54.04821 | 2025-09-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c472fc8-6719-3559-9ebd-926b317f7f8c | -2.12178 | -56.86092 | 2025-09-15 05:08:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f2b3b44-4c6b-31a3-b0da-a442574419f6 | -3.3907 | -50.15132 | 2025-09-15 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f314262-04eb-3845-8f17-373e6834c403 | -4.17956 | -48.575 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d4d4b209-0364-3314-8570-eb862db17d78 | -2.67848 | -54.43621 | 2025-09-15 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 176bd9de-21e8-3f4d-ad46-d0db4a8d620f | -3.65167 | -54.06128 | 2025-09-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c49e73a5-4c6c-3272-9c9c-dc80ac26cdc3 | -4.03682 | -51.03475 | 2025-09-15 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e0d8d23-18c3-34b1-b970-0a2f59e6bf2e | -4.17409 | -48.57711 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86d729b5-cca0-35a7-abbc-61f3a48d5e66 | -5.11793 | -46.12782 | 2025-09-15 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ada9ab6-be12-364d-8f72-750d7d4e2853 | -5.3386 | -45.80583 | 2025-09-15 05:08:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0454b26b-91bf-3cd5-979f-977d082ef7cd | -4.17846 | -48.57583 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d69a168-6bd6-3feb-9a99-0cd906c6e074 | -3.59453 | -47.51241 | 2025-09-15 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7e81182-2800-3c51-a550-a6ee576f1047 | 4.31362 | -60.96379 | 2025-09-15 05:08:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83086540-45ff-3eac-b34e-a3e455984d35 | -3.2221 | -47.63106 | 2025-09-15 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5818bcca-efaa-31db-9438-684521996aed | -4.17973 | -48.56696 | 2025-09-15 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d5a8039-be3a-3740-97e9-c17527c69f2d | -3.52799 | -52.86451 | 2025-09-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 92085076-b146-345c-9570-1a73a9df96af | -3.91132 | -47.71341 | 2025-09-15 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c752db9b-dca3-3140-99da-1e84feb3394d | -2.26129 | -47.84929 | 2025-09-15 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91b17260-15f0-3109-a2a4-33ee5d4f6b4b | -12.00475 | -47.76233 | 2025-09-15 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 884ab700-2bae-3ace-a8f1-d944eb6013a6 | -12.64893 | -47.94897 | 2025-09-15 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ec048d3a-ebac-34bf-aa2e-98bd6e4fd16d | -10.66262 | -46.24312 | 2025-09-15 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fc30fd25-b961-34aa-ba6d-632a8edfa36f | -10.72657 | -44.77878 | 2025-09-15 05:10:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3fc5abb8-f3fb-3acb-b925-07511341fe94 | -11.08033 | -49.73568 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 234c962a-13c0-39d9-9b06-9974fe723600 | -8.95643 | -46.04416 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8f55b4c5-5cae-3b98-91ac-e06240d6b096 | -7.70283 | -44.67352 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3c641e2-fe3a-3fd1-b2c2-dfa6f64bb122 | -8.98584 | -45.81157 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4fc65af6-75ed-3d72-a54e-baaf660ecda1 | -9.05057 | -45.71723 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58f13b0a-03fc-3b02-94f0-b5ac4bd4f26b | -10.73431 | -44.77342 | 2025-09-15 05:10:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d6e493b7-e547-3176-b461-5e19be2c25f8 | -5.63777 | -45.94486 | 2025-09-15 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e126239d-22b0-3f84-9a9a-4f8d0db12961 | -7.88985 | -63.69922 | 2025-09-15 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf8cf47e-e893-3289-96a7-427b27ebb213 | -7.97628 | -45.64664 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9807bf12-5ec9-3924-9fba-e0663ff4b2da | -8.4146 | -47.22989 | 2025-09-15 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d1776a4-ee0b-3b62-be3d-27a3c6ea1e6f | -8.98534 | -45.76326 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c960b5d3-1411-3935-a45a-11779a56cb06 | -7.29537 | -46.58041 | 2025-09-15 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2b373e3-375e-3b62-a37b-3211f2e08107 | -6.97434 | -44.54711 | 2025-09-15 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 33cb8ade-a596-344d-81f5-c8c3444425f2 | -11.31131 | -50.85097 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22aaa561-86e3-3b42-9139-2652feda8623 | -10.08281 | -58.37125 | 2025-09-15 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c6a29c9-c472-3b3c-8261-5dba8d7eee16 | -11.15954 | -57.18953 | 2025-09-15 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26b83e09-0aea-3870-ac9a-09f4f409e055 | -8.59686 | -46.37002 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e0448d9-b093-3f5a-8be1-7aaf777c393f | -8.18428 | -46.76589 | 2025-09-15 05:10:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30ca060e-66d3-3d8d-bbb8-e710dfa4c578 | -4.27045 | -56.00584 | 2025-09-15 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5e9d388-b072-3a2f-acf5-3e4805cf8c4c | -8.64609 | -46.37036 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51f0efe3-32da-3a86-bcf0-bbd90d34089d | -8.62567 | -45.73117 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 776d2342-9ae2-3433-abd9-f1aa42d89b9e | -12.01162 | -46.65924 | 2025-09-15 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa143620-b41b-3071-a285-fe9c5a3a8768 | -10.78598 | -45.9838 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61b10fb1-a2df-38f5-97b1-5fa18c1c539b | -8.11297 | -50.16125 | 2025-09-15 05:10:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7979f66d-2282-389b-9dd1-7c16713b740f | -7.50262 | -55.00581 | 2025-09-15 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2428b63-4254-3dac-aac6-e0a72318dc1f | -7.51691 | -44.36783 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 191cc2aa-956b-33c7-81cf-cdfde3e68ab3 | -12.05291 | -46.54599 | 2025-09-15 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 580c0748-dae3-37f7-b616-cff54c3da26f | -11.44211 | -46.92907 | 2025-09-15 05:10:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fb304f09-d1f2-3cd5-bbac-b8543164b556 | -8.91254 | -45.49981 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 52337235-d583-3f95-987c-87dcb9702c07 | -11.40277 | -51.36297 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 69d84871-c61e-3b12-a150-877285f5506e | -5.84269 | -44.16719 | 2025-09-15 05:10:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d868cbd-ea43-31a0-af93-d9b800b7405e | -5.84957 | -44.16791 | 2025-09-15 05:10:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98138570-3f21-33ce-bb6b-c83fafefe58c | -8.92212 | -45.47671 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bcda0566-12f8-3677-be2b-20e03ebc1489 | -5.63778 | -51.8694 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6acadcbc-1470-3f7a-8df5-5537728d2fd5 | -4.24578 | -54.92274 | 2025-09-15 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README57.md)
