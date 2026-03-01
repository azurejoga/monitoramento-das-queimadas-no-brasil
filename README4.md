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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa33c995-cd19-3aad-9185-581ab7a93529 | 3.31625 | -59.90005 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1089ab9-3d30-31dc-bc78-30a1d6846aca | 2.82799 | -60.77912 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ddecfef0-a204-386f-b6ae-c7daabe84ad8 | 3.3179 | -59.89632 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bbbf78a-a25a-313f-b123-6c19538fb902 | 3.45384 | -60.82322 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ea43636e-4ae2-3c7d-9166-125ed4464a87 | 3.44668 | -60.81195 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e9c73fcf-60ce-3aed-9736-b2c50648ed8f | 3.45288 | -60.81645 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f2e41858-55d4-3db4-9647-3d641c687fc9 | 2.91085 | -60.4294 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3b5776e3-b305-3165-8c4f-3a1305f49441 | 3.45096 | -60.80286 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 073c3e96-7c4b-3b98-8352-4ba824c8063e | 3.48505 | -60.79115 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4ebb0444-6ae6-398d-8b63-97e07b122faa | 3.49175 | -60.77835 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9afba7b4-347b-3f51-8ca8-1741c896630a | 3.15475 | -59.92178 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b9f0f5db-d6f3-34bd-900c-40ef27aace60 | 2.52972 | -60.8128 | 2026-03-01 04:38:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26e2f4d4-a650-3c26-8c0a-6c421e059f3c | 3.16632 | -59.90832 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2ae42f1c-8a41-3815-8331-94f89140bd7e | 2.82894 | -60.78563 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ec3b98d5-257f-3808-9cd9-4b6f9832c00d | 2.82915 | -60.78387 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0cbe7d2c-ad6c-39b2-a660-ad879f764e48 | 3.16221 | -59.92649 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0c7d09ff-9c5b-3b7b-b4d8-047133695bcd | 4.09652 | -59.88724 | 2026-03-01 04:38:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17b6c16d-32a6-3e44-9a53-c541cb693a33 | 3.16716 | -59.91404 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 82a0f0c9-0964-333c-a2bf-4ef1bb49476e | 2.82817 | -60.77738 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9500dc63-b955-332d-80ec-e731b62df5b2 | 4.08976 | -59.88771 | 2026-03-01 04:38:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e931f7bf-a9e3-3b26-8120-d8319ccf0f0a | 2.52281 | -60.81391 | 2026-03-01 04:38:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7a56b05-58a2-3d40-90e6-c32ea542750e | 1.5046 | -59.9306 | 2026-03-01 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 8b3f4e24-1125-3fb3-b3cc-15304033fbb3 | 1.5047 | -59.9116 | 2026-03-01 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 168.3 |
| ce1aaa5b-c367-3de6-981d-2d507c6cc6cf | 1.4864 | -59.9308 | 2026-03-01 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 97.6 |
| fdd84f14-812b-3102-8c24-0552011db2de | 1.4681 | -59.9309 | 2026-03-01 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 7dab61cb-7187-3574-ae29-1ea73f7e564f | 1.4864 | -59.9117 | 2026-03-01 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 131.4 |
| bf75c1c6-2830-3510-88b2-0965a3fb3655 | 1.48992 | -59.92797 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b5815094-0e3c-365c-a104-eeb3d095832a | 1.51831 | -59.93986 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 166e8f95-ccc3-30ac-b844-6a8c5cb11b41 | 1.48426 | -59.93426 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e4e1d08-7e5f-3a16-b12b-9a2fa67e7954 | 1.86842 | -60.40737 | 2026-03-01 04:40:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2dcb523d-a834-3b7d-a39d-5c62a0b9e0fc | 1.48262 | -59.92363 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4c78e991-2f88-3855-ba0e-b78d4328da0d | 1.1984 | -59.97545 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78b3c738-4998-3bdb-8b77-28e4af0c2543 | 0.56865 | -59.91252 | 2026-03-01 04:40:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65713291-3ed2-3a39-9d68-2cc5b16ad8c0 | 1.51664 | -59.92866 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 964cc062-d9d1-3046-a291-5ba648ab054d | 1.51194 | -59.94164 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 155c5280-6288-33d5-831a-b38010eddf37 | 1.51758 | -59.93529 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f5b33686-38e3-3e6d-812f-2994d1ca6364 | 1.48343 | -59.92886 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0b87898b-4c56-305d-a277-4f096ab7e06c | 1.51015 | -59.92953 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bb9b9a81-2827-3c88-bd9b-a9df2f6c631c | 0.47247 | -60.3953 | 2026-03-01 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec3c146d-5814-341f-ab2d-e84091510e53 | 0.89149 | -59.79615 | 2026-03-01 04:40:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7de7ff28-356f-3638-bed9-9091d336e026 | 0.57053 | -59.91207 | 2026-03-01 04:40:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53704b81-15ac-3f63-a945-d26a39ce0367 | 1.49561 | -59.9219 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 9bc831bc-b5f8-3b56-bdac-87d40869797d | 1.87516 | -60.91734 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b950b930-1a71-3cb0-ad2e-f80c196dbb5b | 1.47866 | -59.94097 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 718b5d02-3903-38f0-88d1-1d2049a1b5b4 | 1.08515 | -59.25718 | 2026-03-01 04:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce2ba154-821e-36d3-8182-c58f5baf0711 | 1.09009 | -59.2532 | 2026-03-01 04:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba0f95b0-66ef-376f-b303-84c12d481b3d | 1.87535 | -60.91698 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d31ce754-7d94-36f0-a15e-38a29c98ba8e | 1.06592 | -59.25558 | 2026-03-01 04:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95c92f03-72e8-344c-b1ff-f5053c93659f | 0.85923 | -60.40975 | 2026-03-01 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9f7dd8a4-ba69-32ec-82e4-aa36dd1028b7 | 1.48511 | -59.93978 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 281f163e-5f8b-3fd8-ad63-5047ea4592c1 | 1.20556 | -59.97901 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b53e270-4f5f-3429-a9da-0adfbd5cceb0 | 1.49641 | -59.92704 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 28cbb9e4-4d31-3f30-b84a-6c1884d9f235 | 0.57505 | -59.9116 | 2026-03-01 04:40:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2223b94c-9c93-3b0d-8dac-e2a3d091be13 | 1.49074 | -59.93326 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b11e1b23-ad85-39a7-8261-6ae9c504411f | 0.45279 | -60.39854 | 2026-03-01 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d06e989d-be45-3404-9d5a-bd88c7e2173c | 0.85395 | -60.40707 | 2026-03-01 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cede25e-60d1-34fb-b2f6-fd84a16edcbb | 1.47698 | -59.93004 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d45814f3-96d7-3f63-be41-55cbbc0a716f | 1.5167 | -59.92964 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e40c2d3-ae43-3556-b56c-d8b00bef8d8a | 1.51749 | -59.93436 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44f829a1-e067-328a-a1ef-d06c078ba28c | 1.07209 | -59.25457 | 2026-03-01 04:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44d4f502-0cd3-3459-a5ab-1fa278d09ff7 | 0.45434 | -60.40086 | 2026-03-01 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e049151-88bd-3538-b890-b12317a918f9 | 0.89527 | -59.79158 | 2026-03-01 04:40:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1834c101-8c57-32c5-a35f-1f423824289c | 1.51263 | -59.94627 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 217eba85-4321-3519-9941-cb4d181c092e | 1.88207 | -60.91632 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c061e2b4-d141-3176-836f-93154368663e | 1.08939 | -59.24854 | 2026-03-01 04:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6dbb9a54-b2de-3097-b463-53c0ada58f73 | 0.46592 | -60.39642 | 2026-03-01 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5261ff2-4bc0-3336-9d0a-7b8364cbf5fd | 1.05976 | -59.25658 | 2026-03-01 04:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ffe6cb1-62b4-328e-b8f0-acceb2ac13fc | 1.21131 | -59.97327 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 947b2aea-cd20-328a-9bca-029533ae3a54 | 1.51579 | -59.92378 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 54e30ffc-2c76-3ef2-81c2-67ead4dd7d24 | 1.5102 | -59.93046 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 578c0dd1-a931-3f02-9c6e-d03f32b2c492 | 1.06667 | -59.26035 | 2026-03-01 04:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a87d7cf9-490b-3660-9f6c-2e7c554d0977 | 1.50932 | -59.92397 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 79668f30-c5cb-32d0-8fdd-e6cd8a118439 | 0.57692 | -59.91111 | 2026-03-01 04:40:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b818a0c-23d1-39d0-9adf-9a8abcb6b94b | 1.51099 | -59.9352 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8269772-89e1-32cd-8251-e217ca9515d7 | 1.50205 | -59.9207 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 265c16cc-3e2d-38a1-b91c-9068dc7eb34c | 0.195 | -60.44626 | 2026-03-01 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6a82994a-001a-340f-a8ef-501ca8fcbceb | 1.48831 | -59.91758 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 90f6a917-3cd8-39cf-a0ae-e4c90f6c2adb | 1.50367 | -59.93111 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bebad680-61eb-382b-aa99-cf149d5e91a6 | 1.49477 | -59.91648 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 203bd3da-4d98-3e95-893a-bdfde37eecd0 | 1.07134 | -59.2498 | 2026-03-01 04:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4190406-01e6-34b1-a1c2-ace9b9ba94f7 | 1.09056 | -59.25137 | 2026-03-01 04:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5100c00e-6188-3610-8c95-8d1a554d251c | 1.37056 | -60.31187 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbb13187-014c-3323-95ac-594a4ad5148c | 1.47617 | -59.92476 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| db020675-4e27-3fcf-8807-f380c2479e95 | 1.36395 | -60.31289 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7c0c8ad-c189-3c09-bb47-2207289ff0d1 | 1.47782 | -59.93553 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4fce91c5-650f-3154-9d0b-c2990513dee9 | 1.88226 | -60.91599 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 541dd63d-2319-3312-b2c9-3ceb12f96c2f | 1.49158 | -59.93872 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57e84b0d-0b03-34f6-bfe9-c7dc70da78ab | 1.48912 | -59.92282 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 08bbdc61-b42d-3cfc-9fb6-7ae5ddba67bd | 1.51181 | -59.94078 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a2c26b9-5159-33c7-bbe1-767dca7068d9 | 1.5012 | -59.9152 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 9856ac90-0644-390b-bbc6-b51407aa8fc3 | 1.08441 | -59.2525 | 2026-03-01 04:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d7f35d3-de9f-3444-a8ef-6e1674ccd7fd | 1.49808 | -59.93785 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9c28b07-78dd-3f1a-adc5-dba95477b7ef | 1.50284 | -59.92579 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 9c13431a-7c89-35bd-8e2e-5e0b34515e99 | 1.50933 | -59.92488 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 61683209-108d-3338-8b81-6f345c073e85 | 1.46977 | -59.92627 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bbeaa1c5-5d1a-3e05-8b77-a7f7124ea638 | 0.18844 | -60.44732 | 2026-03-01 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 795ace57-53b7-3768-9627-b12222024e7a | 1.50456 | -59.9369 | 2026-03-01 04:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d555daa-fbe8-3011-8271-fa2f16f5d00a | 0.45343 | -60.39526 | 2026-03-01 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 731f9c44-42ef-337f-928e-26b7d906a4a7 | 1.0605 | -59.26134 | 2026-03-01 04:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38eb12fd-d14c-3790-886a-566528d10f20 | 0.19412 | -60.44075 | 2026-03-01 04:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |


[Clique aqui para ver as próximas entradas](README5.md)
