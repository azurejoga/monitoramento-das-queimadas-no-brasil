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
| 9b86e76d-5783-35f8-82eb-11dd846cbf85 | -13.63191 | -56.94637 | 2026-08-11 05:29:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d82eab00-1a83-3bef-9670-7eeda5a01138 | -11.24447 | -54.8775 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23135d74-0c70-37cf-ba87-d67fae2f79b1 | -11.60968 | -54.65724 | 2026-08-11 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e54e10af-df2f-3d54-9809-d38c9d0f172f | -10.72581 | -50.43878 | 2026-08-11 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe2fed47-9e62-3bbf-b656-db8c7ea9b14a | -11.615 | -54.6529 | 2026-08-11 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b64a5990-c3fc-3f7f-986c-232bf79c6ce8 | -8.95338 | -60.50918 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6c046d6-543d-305a-9511-29c72f5455b0 | -13.87216 | -53.77979 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9b80455-8d61-3aec-be7d-164485f0c40e | -8.9462 | -60.53328 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc04373f-a743-384f-bf90-357fbd97cedd | -11.23009 | -54.84408 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfb00419-e235-3a46-8686-7f611ae5dd19 | -9.47454 | -60.51852 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d339ee67-b43b-34ae-b566-189053b1eae8 | -14.16717 | -54.03022 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c86a61df-36ff-352c-8322-b568b08fdc4a | -14.39898 | -53.39578 | 2026-08-11 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9122f501-6332-3ad2-8d2d-65cde0056450 | -13.8639 | -53.80486 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b4aff71-b8c3-3432-be3f-7272470abb33 | -10.14802 | -67.72652 | 2026-08-11 05:29:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7c6398e-54fb-322d-aab8-0fd8b6833eed | -8.67949 | -62.86875 | 2026-08-11 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89696be0-a05c-3192-a55e-316ed5335ce3 | -8.95115 | -60.5016 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abbc48fd-2931-30e7-bfb2-ddfa9d420242 | -13.87291 | -53.77367 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5aeafe99-07b7-30e3-927f-fe902d919310 | -8.9517 | -60.49809 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a7c6cc82-cd30-3049-a4b6-46564e6c4124 | -10.27641 | -60.53836 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 981a109b-81aa-320f-93ed-8bf35312299d | -9.37368 | -57.36591 | 2026-08-11 05:29:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e103688c-9ba2-33b8-a27a-fef5cc61f58d | -8.89417 | -60.56107 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5118f072-64f2-3a8d-8432-d4b828c6bf6d | -11.23141 | -54.83462 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e62375bb-cfd6-3573-b7b0-024dd31e5845 | -13.85919 | -53.80094 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 47d4cd23-c193-3ee4-a68f-8c6a01c0b33e | -14.16681 | -54.0331 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbbb4e3d-0e30-3dfa-9710-28a5a02d906a | -8.95845 | -60.58564 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69bc1020-ab39-3f34-8442-529d73d027da | -10.72637 | -50.4341 | 2026-08-11 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 862db109-5ef4-3470-8a9b-cd32595a9996 | -14.31029 | -54.91264 | 2026-08-11 05:29:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 54e1b71e-9489-3982-9aa6-fc60c42b8638 | -8.89475 | -60.57916 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3841f0dc-88ad-3a19-8352-639d52005c2f | -8.95673 | -60.53133 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 272b73ec-7046-308b-b40d-955cccf1ab2c | -8.94673 | -60.50812 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7258a712-477d-3b4f-8b16-1068b86ea41a | -11.61033 | -54.65226 | 2026-08-11 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fcd7d8e-a7dd-3866-bc9b-fdcd6b3bccd9 | -10.73077 | -47.91536 | 2026-08-11 05:29:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 91d3b9f2-4371-354f-b3b0-7ce260f63f20 | -14.30886 | -54.92172 | 2026-08-11 05:29:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 314cb4b1-f4ac-3f42-9e28-960546af3fac | -9.47179 | -60.53621 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 272dc1a4-df8c-3d8f-9ac5-71d5fd19ce8c | -10.07541 | -60.5 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c37cd72e-d14e-3579-8618-a766322408fd | -13.84173 | -53.6864 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4f3f258-3d46-3418-9daa-120089dde323 | -10.89519 | -50.37564 | 2026-08-11 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fdd2851-8058-36ec-9395-86c256f3a856 | -8.95842 | -60.56404 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 34a1becb-c509-3f03-b43e-40afb1f39392 | -9.07151 | -65.4539 | 2026-08-11 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| be2b897b-e4aa-30f0-9d9a-dd7ffd9037eb | -8.9506 | -60.50512 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2f8610e-aa91-34d3-b011-8048839f9d26 | -8.89644 | -60.59022 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b27f9565-e7f3-39d2-96b2-29d09b675534 | -13.42808 | -57.04715 | 2026-08-11 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a5f73de-693c-3532-bde4-2dc3270108af | -10.93756 | -57.11791 | 2026-08-11 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00d70294-829d-3b11-89f2-99b660128c74 | -8.89753 | -60.5832 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1d83d13-2239-3342-a5a0-d853f731b0ca | -14.00406 | -53.98506 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bcf1275-e4c6-313b-9fc6-78db6cea46da | -13.8702 | -53.79585 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ea2fc35-204e-399e-8982-0e6ee157c55b | -14.31363 | -54.92232 | 2026-08-11 05:29:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c5a75ee-bdae-3a89-9a12-08b77adaec5c | -8.95453 | -60.5454 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a669d2ff-55fd-380e-8fe0-f1cdbce6c408 | -8.95508 | -60.54188 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 94227917-5505-34f0-94a6-64f6ad83b4da | -8.6789 | -62.87241 | 2026-08-11 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0beb8ac3-eed7-3ca4-b3b7-f27f14e0d75a | -9.47176 | -60.51445 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc3cc4f3-c758-3f40-8919-a662d1822e52 | -9.47069 | -60.54327 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c8318ba-7d0d-313d-a2a7-73a8ad501574 | -9.47457 | -60.54027 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6beb8e5-a925-3ec9-b772-32f5caa3913c | -13.86303 | -53.76937 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b0f6261-3999-360f-826a-e4ca3297fda0 | -10.88963 | -50.37011 | 2026-08-11 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a953bf9d-4f5b-3546-9897-a283abd71582 | -14.31432 | -54.91699 | 2026-08-11 05:29:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b251c484-2cda-3152-821c-4f48c0e27dbc | -9.47121 | -60.51799 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18ec1fea-6eb8-39b7-9c10-19d0f7fcddc4 | -8.94453 | -60.52219 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c64de12-ad5d-3422-b55c-360b0cdba8ce | -8.95785 | -60.54593 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b8bcc4d1-7814-3fba-94f9-4ae2e7c4919f | -13.43624 | -57.04836 | 2026-08-11 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b84f888-a581-347c-93a6-f4a61743fef0 | -13.84098 | -53.6927 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2cd8499-7182-3d3f-8146-b8a6eb54c32b | -9.47399 | -60.52206 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6ef5b4d-6034-3d94-83d7-8ad3f2f29566 | -9.37434 | -57.36131 | 2026-08-11 05:29:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d1f3ef8-bb76-3f14-a4cf-2293547cb0b6 | -8.94288 | -60.53276 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e95f302-992c-3628-9a62-cb544beed23f | -8.94898 | -60.53732 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bea19e2-b7b7-3a2b-9b42-991eadacd3fa | -9.47234 | -60.53267 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3f03dbc-38fa-352c-bfa6-b446773685a6 | -8.95503 | -60.49861 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 84074ee1-a2be-3520-a4db-36fa565e6e6c | -11.19607 | -54.85386 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13f82955-ef45-3fc2-95d7-cf95f483cfdc | -9.72354 | -60.20252 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22ff499c-5876-3dcb-9d28-dd754aa808f4 | -8.9573 | -60.54946 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d7d1e6dc-098b-3c0a-ad94-f4202705f2eb | -8.89472 | -60.55756 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d23a52f2-fd5e-3f41-942c-9429314369d0 | -8.96173 | -60.54294 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19f84a6a-1a76-301f-bc3d-0bd2f78a9dba | -8.94843 | -60.54084 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8466c2af-75a4-37cf-88c8-eef7542e0c38 | -9.47124 | -60.53975 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1842199c-1358-30b8-a8ce-328784b341f5 | -8.89808 | -60.57969 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52046eb4-a250-37e6-8577-53e1d8d230fc | -13.8647 | -53.79833 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76e62ef1-1c8b-3b21-ae46-6ecf1273dcce | -8.95565 | -60.56002 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b271d832-c56f-3127-8b19-d9b75848954a | -13.87572 | -53.79317 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bb0ec69-4d59-363b-8901-9658b3329781 | -10.72553 | -50.43563 | 2026-08-11 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77bc4ef0-1949-3906-8b3e-3dc771ee1015 | -8.95781 | -60.50266 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d383c1e-8515-317b-b996-d82c6f109342 | -11.22943 | -54.84884 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b73ad435-da20-35b5-9a1d-baab61d54340 | -8.94565 | -60.53679 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02683d80-0f7d-3a6a-94f6-b08109e7385b | -8.89421 | -60.58267 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 014f55cb-decc-3f01-a0f0-116878c3a348 | -8.95732 | -60.57106 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf0aa2aa-c136-3be0-892b-048ac61ae299 | -9.72018 | -60.20199 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af774b43-5137-3f7c-afe7-6298bb595ebf | -8.89863 | -60.57617 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f72436ad-9f92-375d-b632-5a51acb8537a | -8.95558 | -60.49509 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 846a1d38-159f-316f-9c5b-8f3aa28d1f47 | -8.9595 | -60.53538 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4c6e080a-ed4c-3c36-bf12-6f2967264a14 | -9.46956 | -60.52861 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9e6824a-bd44-3234-b32a-92e9f929b8d7 | -8.95175 | -60.54136 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2269a48f-22f1-309a-9fee-ccb13956aec3 | -8.95232 | -60.55949 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2aedd2f1-2c16-3fb5-bf5d-a5be261625c9 | -8.6817 | -62.87663 | 2026-08-11 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a71c3e7-8482-3a7d-9804-b553f151be1a | -9.25167 | -60.33442 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49de6797-b0a5-31fd-959e-b7a42a252445 | -13.43674 | -57.04465 | 2026-08-11 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec5a1b33-475f-34cf-ad0b-d230af29e5d9 | -9.89648 | -60.26637 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 484d8ee4-cb82-31ee-bcb5-701e75ea7fd9 | -9.89984 | -60.26688 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f521140-db1a-3b88-a804-afee59ee9731 | -10.73011 | -47.9211 | 2026-08-11 05:29:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0c38f857-ccaf-3f4b-a392-ca74705a713f | -8.9584 | -60.54242 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d99b4a4-9538-3c82-a6c2-a8bf469ab10c | -11.60501 | -54.6566 | 2026-08-11 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2009d6be-88f0-345e-a642-f194427a3ab7 | -13.87651 | -53.78675 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README29.md)
