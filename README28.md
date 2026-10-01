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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00fa7547-e691-3726-8bf3-a6b27980f7de | -3.24923 | -50.81413 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9396977c-da8a-3404-b534-f3036d5539c5 | -3.93568 | -45.42117 | 2026-10-01 04:12:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d6772fd9-ec7c-3fe7-9c66-b68af1ec758d | -4.12745 | -46.86869 | 2026-10-01 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef2e3070-b524-31af-b2ef-ea0a1e71cbb4 | -3.10091 | -50.29679 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f463c44d-b8a1-3aa1-8cfa-6cb8f5a89a0c | -3.10243 | -50.2876 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a74a979-f664-37b2-b04c-00d3c9a62d16 | -3.09377 | -50.26107 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2649f413-684c-3748-8519-6332d138ad0e | -2.91615 | -51.31863 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b65681d3-b79d-3a7b-9fc5-8a269911061e | -3.21972 | -48.81736 | 2026-10-01 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c82c84f-0481-351a-80d5-94f11778c893 | -3.95644 | -48.12587 | 2026-10-01 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5a6545ad-6bfd-388e-91ab-e6504ee74335 | -3.25611 | -48.77151 | 2026-10-01 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf9e760e-1129-34d8-a713-4b246c438c4d | -3.09216 | -50.27036 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eeeb5683-1e94-3180-a390-13c7933a1871 | -3.18067 | -51.24958 | 2026-10-01 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff1d908b-f4bc-30aa-8a7e-9b07c8ea5e46 | -2.98021 | -51.02429 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a148866-3cf8-3de3-95a3-c9c5a242b217 | -2.3009 | -48.58548 | 2026-10-01 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae4e25b3-b8f2-3963-a64f-506f4f9096b3 | -3.37391 | -50.94754 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecf830cd-854a-3454-8ee3-dd052fba96ac | -2.91823 | -51.31627 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f99a313c-d4ee-3ee4-8ff2-c397f76cd443 | -2.98474 | -51.03866 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 988a7476-d2ea-3c64-ae9d-b3d627d4b32d | -3.10967 | -50.27813 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 59f74099-e7be-33de-9915-77d4bcbc9ee0 | -3.37864 | -50.94793 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1889ed8-113e-3ba2-b19c-781dad376435 | -3.42092 | -48.33611 | 2026-10-01 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ef40588-1087-3836-b70c-7c714d3548d1 | -3.08717 | -50.26606 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f004a28-4bb7-3fb1-b54c-2be898345f15 | -3.68857 | -47.12903 | 2026-10-01 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91c57c5c-080e-3b0c-bf63-98c44d17f0df | -3.16294 | -51.35228 | 2026-10-01 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 661b321a-67a5-3be3-8471-8f6f548cc909 | -2.97587 | -51.0504 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ed3a2ee-bafe-30dd-873e-cd07eca2327c | -3.37931 | -50.95396 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be89644f-b12a-36d9-8a9a-3a9e0a312b7f | -3.11817 | -50.26526 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 64d16f9a-1701-3ce5-b4cb-33e09bf5e5d5 | 1.96881 | -50.86652 | 2026-10-01 04:12:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd6cee9b-d952-3a2a-9ccb-54566150b658 | -3.1073 | -50.29182 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d7e906b1-6a71-3298-b8bc-8a2fd44a86df | -2.27514 | -48.75295 | 2026-10-01 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39da63b1-2f99-3239-aa7e-e2cbfe6fe2e3 | -1.90273 | -45.81081 | 2026-10-01 04:12:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a9a1d3f-a642-3560-826b-2175d8d6d0b0 | -2.96829 | -51.01676 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6d251da-419a-35e4-af82-3346138d1a17 | -3.38114 | -50.9436 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a531f196-df48-335c-8928-14c16b3ae802 | -3.26888 | -50.70022 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc83cb02-538d-34eb-8bce-bb714d54931a | -4.14 | -48.91088 | 2026-10-01 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 501fd571-7f9a-3308-a9e5-823557e20e16 | -3.11896 | -50.26065 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 114ea278-9d9b-38ae-9bd5-d43e3e92b803 | -2.91171 | -51.3151 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ecb4546b-1922-3df0-96fd-020372a22580 | -4.94704 | -36.98106 | 2026-10-01 04:12:00 | NPP-375D | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 810a641f-181e-3982-b538-65aa263c619c | -3.04897 | -39.92953 | 2026-10-01 04:12:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8249c4ee-609e-302a-9d81-06e3b02b2048 | -3.08794 | -50.26147 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d75ea07-549b-3ff6-ba8a-c5af911a25d0 | -3.82223 | -50.62033 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c6caa2e-b51f-3fc8-ae6e-030e3398a90d | -1.90194 | -45.81554 | 2026-10-01 04:12:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0b86107-307b-3405-95ec-28a1ea596125 | -2.34924 | -45.8584 | 2026-10-01 04:12:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2218aa93-55dd-3093-af1b-844dc4ae4b97 | -3.03395 | -48.41595 | 2026-10-01 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 451e0d1f-c21d-35fc-b9be-c2ab92027f24 | -3.95807 | -49.45324 | 2026-10-01 04:12:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7364ba23-718e-33fe-a206-81c958638893 | -3.25009 | -50.80911 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf9f563f-5695-3472-bd3a-bed785c55ff9 | -3.37776 | -50.95311 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b32ba925-e6b1-3c2e-bacb-742f707a3bc1 | -2.96823 | -51.01977 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54087fa2-f9c5-3030-b8df-b65720093ee6 | -3.11046 | -50.27354 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e00f337-ba03-362a-b83b-47b0b21437bf | -3.95946 | -49.45276 | 2026-10-01 04:12:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7f43cac-0d4c-39a0-aec8-3e2c69a118bd | -3.5507 | -48.17496 | 2026-10-01 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7e0ce97-47b1-3e5b-92fb-2681158b55b2 | -3.96166 | -49.05894 | 2026-10-01 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c5cd235-3446-3ad7-a3ba-8931372c3a20 | -3.26802 | -50.70519 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73c6bcf0-f5b0-3512-8ec2-c0765ce31f6f | -2.98107 | -51.01912 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7127861d-41cc-3e75-aaf7-c3706a36897d | -2.97208 | -51.03356 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3968406-9629-3dd0-8a27-f2766a3322b7 | -2.91733 | -51.32167 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 482e1d08-d3d1-379a-829d-0ffd30fcc4aa | -2.91057 | -51.3121 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2af81e04-5722-318e-a919-dad6aeb6b27e | -3.08686 | -50.26472 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc04944d-fe63-35b7-bd75-80cbfb2c04f7 | -2.97282 | -51.0313 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e9c9f65-4efb-3f51-be65-5e298f7a3d10 | -3.8284 | -50.62135 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18a3d9b9-52df-363b-97b6-d0ad40f6fa07 | -2.30078 | -48.75572 | 2026-10-01 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2ea5b3f-6aad-3cd8-95ae-48496d891e7d | -2.44861 | -49.21674 | 2026-10-01 04:12:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e4fd57a-13c1-3a50-bed3-ee4912d7294e | -2.91081 | -51.3205 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a5f6b98-b748-37c3-8097-41f1284fe829 | -3.10624 | -50.26461 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce68e446-1236-31dd-8e16-84bfb96251fc | -3.34527 | -42.40456 | 2026-10-01 04:12:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bd31c02d-0b51-34b1-8096-7561b736d869 | -3.56608 | -51.4794 | 2026-10-01 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7674c076-0ac3-3cf4-8b71-5f235d9710e4 | -2.22095 | -46.07146 | 2026-10-01 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d69e512-bae5-300f-a084-caab32a5fbc6 | -2.96551 | -51.03538 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06b12a90-c6cd-3080-8f4f-cd0d4f0a4e00 | -3.11207 | -50.26422 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1438aa2-190a-3225-b6bc-8ed9af8d1df9 | -3.95737 | -49.05063 | 2026-10-01 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1350f45c-5b8c-366e-9a2e-1451db6306c8 | -3.10436 | -50.27248 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49b89529-f5df-3f3a-9249-ec344e54936c | -3.1047 | -50.27391 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea011b40-82b9-36c4-9ad3-bd55fccdd04f | -3.24998 | -48.77408 | 2026-10-01 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c9f6dc1-9e02-3fdd-8bf8-0f2626e255ab | -3.10015 | -50.26352 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63b85962-2ef0-35c5-b469-2aeaff3b23c1 | -2.97849 | -51.03465 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0cb3375-c33b-30a5-afae-341bb9e07ee7 | -2.96732 | -51.02499 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1eca174c-239a-3004-ad21-5b03717f837d | -3.11578 | -50.27912 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 03b25a0e-7d70-32ca-b1bf-872f5660ce8a | -2.83377 | -50.47038 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| def2e251-b066-36b6-a1b5-0e901839ddab | -3.10168 | -50.29217 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 624bb32a-67d2-3975-a7dd-bf9b539fec51 | -3.3489 | -42.40518 | 2026-10-01 04:12:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b490c202-c667-3d8b-b9fd-dc169204def5 | -3.9761 | -41.51658 | 2026-10-01 04:12:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 737f2c0a-8def-3acb-abb6-c71a69c81f29 | -3.96228 | -49.0554 | 2026-10-01 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b3b28c6-f0c0-39a5-be21-f96ac4a320a1 | -4.15952 | -48.89587 | 2026-10-01 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d59d0956-b587-3a62-81d5-4b3f7e3b67c3 | -2.97924 | -51.03236 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7da5c14b-0426-3c25-bc30-0922aef8b14d | -2.35691 | -45.86923 | 2026-10-01 04:12:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8cfd8d0-8ea0-3376-abf2-42db41022432 | -3.18156 | -51.24443 | 2026-10-01 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44615ff3-65d7-36fe-a06e-00906d6bdf86 | -3.80331 | -51.02917 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7c120d9b-fb67-3fc0-849f-d9cd8f700a1a | -3.3784 | -50.95908 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13dbc216-6a1a-33a9-bb6b-a58e5991afc8 | 1.96692 | -50.86173 | 2026-10-01 04:12:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5801cb3b-e414-35a0-893b-cc7e95cea3fe | -3.11419 | -50.28835 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a1e9d127-e5b4-3f9b-a64a-785f231069e5 | -3.10596 | -50.2632 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ff329cc-7123-37e7-bff8-67a2b9135504 | -2.96567 | -51.03244 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 033d6679-83a2-3c56-8a38-dd17a3add772 | -3.01242 | -51.46586 | 2026-10-01 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6031cc93-1790-36b1-b0e5-3c2b7eb3e9ea | -3.12191 | -50.28005 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9022e268-3cfc-3352-bcf4-e6c523b3f16e | -3.54588 | -41.56787 | 2026-10-01 04:12:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f317e689-9cc2-3b84-b17f-6248390f2804 | -1.32511 | -49.12801 | 2026-10-01 04:12:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fb55889e-fe8f-3612-86ec-a0884c47ac80 | -3.09987 | -50.26211 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef93ddc2-510a-35aa-805b-c14cb36e3bcc | -2.98653 | -51.02833 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d9aa4afc-6f98-348d-bbc0-3b0c2b5cc0ca | -2.98102 | -51.02204 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae19f7b5-fff2-3609-b678-4fc3709303a0 | -3.10041 | -50.29531 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 69615b76-ad9f-3bbf-921e-162dceb36062 | 1.96998 | -50.83643 | 2026-10-01 04:12:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README29.md)
