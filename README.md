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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2c30323-6fe0-313a-af91-07e9643ea09f | -8.9212 | -60.7681 | 2025-08-06 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| e5ffb8eb-c284-374d-b60a-9272564cca40 | -8.9213 | -60.7489 | 2025-08-06 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 205.8 |
| 854ace2d-a34e-3ceb-9263-f5464601294a | -16.3268 | -50.3481 | 2025-08-06 00:00:00 | GOES-19 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 70dba3f4-5bdd-3675-881f-9f5192abd0db | -9.693 | -48.8787 | 2025-08-06 00:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 82dfd920-1c5a-343a-be81-8382d516b1f4 | -13.0538 | -56.8746 | 2025-08-06 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 103e7688-320f-3285-aed5-d87a293d310e | -12.7576 | -44.402 | 2025-08-06 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 8512631f-6ea3-308a-aca0-3ebfdb92e327 | -9.0646 | -45.052 | 2025-08-06 00:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| dab90dfe-b7c5-369d-9e1e-8c68b690de66 | -12.0382 | -44.8189 | 2025-08-06 00:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 3eba7a4c-928c-32bc-9a4a-a7b10608dfa6 | -13.0731 | -56.8527 | 2025-08-06 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| d96472b7-310c-3435-a689-089bb8c264b6 | -11.4389 | -45.1385 | 2025-08-06 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| d11d94f9-df66-3de6-9c8a-533fd86e321f | -13.7363 | -53.1729 | 2025-08-06 00:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 3231d15b-97f1-39ae-9874-4d2ec30109ca | -7.8383 | -45.0899 | 2025-08-06 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 7b698dbb-cf58-3d82-944e-1ceb670f09b8 | -9.7119 | -48.8768 | 2025-08-06 00:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 79b18f7c-086a-3815-b38a-28caa56d8cc4 | -13.054 | -56.8545 | 2025-08-06 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b98fdc6d-6fc8-31cb-9e42-4ebf33fe4160 | -8.9215 | -60.7297 | 2025-08-06 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.0 |
| bb89ad77-6270-3588-97ad-d09dc632b178 | -6.6154 | -45.3354 | 2025-08-06 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 6b241b34-71b1-3c52-8130-67851038030c | -8.9028 | -60.7498 | 2025-08-06 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 7ae1aec0-a227-3af6-9f3d-6fa160609462 | -13.0728 | -56.8729 | 2025-08-06 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 68bd9998-e6e6-3831-97db-bad101310da4 | -13.7366 | -53.1519 | 2025-08-06 00:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| fcbce92a-c757-376c-9264-82ef80f3c68c | -6.9492 | -51.6302 | 2025-08-06 00:00:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 910f981e-e652-3335-90be-7c0507ab55d0 | -11.4393 | -45.1154 | 2025-08-06 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| b3918f1b-1775-35cb-819c-a892f6740414 | -16.3465 | -50.3449 | 2025-08-06 00:00:00 | GOES-19 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ddfdb302-ccb0-3077-b8b5-da1a33c65773 | -9.0835 | -45.0499 | 2025-08-06 00:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 3b2da5d7-0761-30e3-b497-e13c65bada74 | -12.0189 | -44.8219 | 2025-08-06 00:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 3119ca44-c853-3878-9cc8-bad80a70edf7 | -8.9213 | -60.7489 | 2025-08-06 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 193.5 |
| 2fee95c8-15f6-3eac-ab81-f25924c894b7 | -13.054 | -56.8545 | 2025-08-06 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 3d1ddf86-6e6f-30cc-ac7a-afa149823bfe | -16.3268 | -50.3481 | 2025-08-06 00:10:00 | GOES-19 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 68b8799f-5514-32fc-8397-b1084c08c20c | -11.4389 | -45.1385 | 2025-08-06 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 559381af-8c28-3981-a841-184f2c0400c7 | -16.3465 | -50.3449 | 2025-08-06 00:10:00 | GOES-19 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 29443bd3-bb16-3b51-9e31-14e500cdcb9c | -9.0835 | -45.0499 | 2025-08-06 00:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 2eeffbb5-cca1-3709-97cd-47dc150d2027 | -11.4393 | -45.1154 | 2025-08-06 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| f081b406-c5ef-3afc-bbf2-2063db9fecdf | -8.9215 | -60.7297 | 2025-08-06 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| d662c4cc-213f-3dc7-9e7f-7932567153c5 | -13.0728 | -56.8729 | 2025-08-06 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 416a8a76-2e61-3197-bc16-37fab0cb3958 | -9.693 | -48.8787 | 2025-08-06 00:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 28bf51dd-f788-3337-b7e8-952f81348a13 | -6.9492 | -51.6302 | 2025-08-06 00:10:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 3c1600e4-bec3-3d9f-a22f-8d25d7c86844 | -13.0731 | -56.8527 | 2025-08-06 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 2676ea21-628f-3153-b7a2-bef23019d2c5 | -13.0538 | -56.8746 | 2025-08-06 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| cc8dd8bb-75b8-3a82-97a1-b64edc556d96 | -7.8383 | -45.0899 | 2025-08-06 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 3d13f632-6efd-3fa9-a12b-42618cbcdc0d | -12.0189 | -44.8219 | 2025-08-06 00:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 01867c0b-2c00-3f1b-80b2-85bebff00000 | -8.9028 | -60.7498 | 2025-08-06 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| e860ca47-ce17-3407-a299-9463bc9c2cc4 | -8.9212 | -60.7681 | 2025-08-06 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| a764dd44-ef33-31c3-9c98-1d9b1f23244c | -12.7576 | -44.402 | 2025-08-06 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| a641f760-0a65-3d9b-9257-e4919fcb558c | -9.693 | -48.8787 | 2025-08-06 00:20:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 8cf04966-5645-3430-9f9a-2f65fc462b8c | -11.4389 | -45.1385 | 2025-08-06 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| a4122773-3643-3285-b95d-6ebceeb5ad29 | -8.9028 | -60.7498 | 2025-08-06 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 5099bdb2-dabc-32b4-9a5b-a7f7d2149a17 | -8.9212 | -60.7681 | 2025-08-06 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| e1ea6549-6bf8-3866-9d47-9ab6e2c05c1c | -7.8383 | -45.0899 | 2025-08-06 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 758ddd33-b3cf-37ef-a268-b9104f5b3c2e | -9.0835 | -45.0499 | 2025-08-06 00:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| e6ddb44e-0cfc-31f4-9b60-2c557bd5e49c | -13.0538 | -56.8746 | 2025-08-06 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 0b2c757f-8852-3567-b368-d4de8bafec81 | -6.9492 | -51.6302 | 2025-08-06 00:20:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 0ef8f1dd-a382-3481-9ddf-42fb66c62af0 | -13.054 | -56.8545 | 2025-08-06 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 22961195-23ca-3a4a-b318-ab43318eb1f6 | -11.4393 | -45.1154 | 2025-08-06 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 9bcb9b03-928f-3e7a-9a6b-f814d394b5d5 | -7.8194 | -45.0917 | 2025-08-06 00:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| d2d8cf06-aaf4-3df6-9dc2-d6e8c80b3944 | -16.3268 | -50.3481 | 2025-08-06 00:20:00 | GOES-19 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| a3a67af6-1070-38a0-909f-97c816b4a739 | -12.7576 | -44.402 | 2025-08-06 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| e6790f1a-3bc2-33c8-ba68-396cb0edc77f | -8.9213 | -60.7489 | 2025-08-06 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 181.9 |
| e648e384-7faa-3fc6-9571-71d65117f2fa | -12.0189 | -44.8219 | 2025-08-06 00:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 17fb5598-c4d1-363a-8327-b17d894d8f6e | -13.0728 | -56.8729 | 2025-08-06 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| af9b7fe0-c7ed-3853-bb4f-75d9fd826ad1 | -13.0731 | -56.8527 | 2025-08-06 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| d1ee1b7a-bbe8-3cb8-9055-0464c44583d5 | -16.3465 | -50.3449 | 2025-08-06 00:20:00 | GOES-19 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| bb659a45-508d-3e43-9940-8c17722699a9 | -8.9215 | -60.7297 | 2025-08-06 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 1827263a-fa4d-3299-83ce-14c436e44f30 | -16.21851 | -41.3454 | 2025-08-06 00:24:00 | TERRA_M-M | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 51735c00-bc94-32b8-8870-c9c59ea9e9cf | -16.25276 | -39.04641 | 2025-08-06 00:24:00 | TERRA_M-M | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 780e7f2b-7efe-324d-9edc-4ab4e6d4e1e7 | -11.84426 | -43.72892 | 2025-08-06 00:26:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 7738df95-e45c-3002-a477-82e1f4e3da5d | -9.6991 | -48.87024 | 2025-08-06 00:26:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 57f5b7f2-da2e-386c-92bd-03d0e4a5bf1e | -11.50833 | -50.28634 | 2025-08-06 00:26:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 249a6337-875c-3f60-8149-95bb5c275d02 | -11.42794 | -45.13441 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| e7bd290b-5818-3138-b981-1f9b31465a3a | -11.73681 | -47.52509 | 2025-08-06 00:26:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 2aeb5394-e6f3-3980-93e9-ded73c6aa0b2 | -10.77963 | -46.63273 | 2025-08-06 00:26:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| cde2eea0-40d8-3786-bcb8-ae97c8f76cef | -10.4437 | -44.36924 | 2025-08-06 00:26:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f2c54c78-759d-3b78-8c0d-cc54eab339da | -13.36941 | -43.75508 | 2025-08-06 00:26:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0ce45f3a-1ffa-3c5d-b2fe-f5930524f6e6 | -9.1839 | -48.84666 | 2025-08-06 00:26:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f80fac17-8a8d-3cc6-b48d-bafb6371fcec | -12.53708 | -47.17959 | 2025-08-06 00:26:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 64c33c56-160b-370a-b42f-77f437b988a2 | -11.90826 | -44.94262 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| bb329ed4-2c63-32c3-93d6-f6a1a255c03f | -13.29854 | -43.84486 | 2025-08-06 00:26:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 70325e46-2016-3e5b-9cc1-203905355be5 | -8.99215 | -45.6936 | 2025-08-06 00:26:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| db463931-109d-32c7-9569-773c6f4453aa | -11.92631 | -44.03609 | 2025-08-06 00:26:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f0235045-d9ab-3f95-9d14-5d107ecbae4e | -12.75453 | -44.41586 | 2025-08-06 00:26:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 890abd04-91c2-3299-9137-04313ae2f2cd | -10.12251 | -51.67563 | 2025-08-06 00:26:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 40d821d0-1c0d-399a-a2c2-dafeab7dff38 | -10.31579 | -50.38298 | 2025-08-06 00:26:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0b673ec6-5647-35f7-b597-76e551dfc0ad | -11.73812 | -47.53495 | 2025-08-06 00:26:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| bf70111d-0a41-3d22-a94e-dc7fdc2e76e8 | -12.04236 | -44.01624 | 2025-08-06 00:26:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 851f8308-7c13-3ad1-894e-19c8293300a8 | -13.7643 | -42.57777 | 2025-08-06 00:26:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| cbec52d8-d6c5-3f50-8d60-5bac4031249c | -12.40839 | -44.70018 | 2025-08-06 00:26:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dd8dae43-f673-3a2a-87c5-03cba80895a6 | -10.46697 | -44.33644 | 2025-08-06 00:26:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| da2c1e4d-24c7-33f6-a5dc-a338fbbb183f | -10.11746 | -51.68277 | 2025-08-06 00:26:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7d755b65-59fa-34f6-a8c5-3604595065be | -16.33806 | -50.34665 | 2025-08-06 00:26:00 | TERRA_M-M | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 727d2204-70c8-38d0-add5-69e23bb6c492 | -14.08804 | -46.33423 | 2025-08-06 00:26:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fece1be6-5a65-34a2-a861-771c9e8a2c32 | -12.7635 | -44.4145 | 2025-08-06 00:26:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| ee646726-3331-3019-b424-d54bcafa3a90 | -13.29994 | -43.85443 | 2025-08-06 00:26:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| cdc00fa9-61b5-391c-8f71-20fda336f43a | -16.32617 | -50.34824 | 2025-08-06 00:26:00 | TERRA_M-M | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 95.7 |
| be7b3519-f054-3eb9-b623-30b226746971 | -10.53257 | -42.55287 | 2025-08-06 00:26:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 26.3 |
| 21890e21-0072-3b2e-80da-454799a2c6b6 | -10.65038 | -45.23338 | 2025-08-06 00:26:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 80317f90-d631-3449-a907-aa927e298b25 | -12.71854 | -48.07821 | 2025-08-06 00:26:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 79b65b0c-6872-344c-9657-e0b5d794d6f4 | -11.03075 | -45.05974 | 2025-08-06 00:26:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b4e106ef-9ca4-344a-a89d-6712fd332e8b | -12.38142 | -47.05097 | 2025-08-06 00:26:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c7a36dfe-f43d-38e1-9ea4-9ff4a2d18287 | -9.07571 | -45.04598 | 2025-08-06 00:26:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 704ba3f6-decc-3b86-a447-2bdf7c2f73ae | -9.07705 | -45.0554 | 2025-08-06 00:26:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 2e1221f2-180e-380e-9542-7ec27fc0f9d6 | -10.44507 | -44.37875 | 2025-08-06 00:26:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 73c27e7c-2af1-3ee9-abdb-3ad1586a3f88 | -9.64998 | -43.8516 | 2025-08-06 00:26:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |


[Clique aqui para ver as próximas entradas](README2.md)
