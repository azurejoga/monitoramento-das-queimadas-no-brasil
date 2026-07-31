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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbdc32ab-39a9-321f-9eec-8871760c8102 | -14.39794 | -48.06025 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c7baac8-0c3e-3430-b9c4-4c151413cb1b | -12.62273 | -44.62965 | 2026-07-31 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15be0cfa-1bcc-328f-a8a1-669b9f7e2544 | -12.62197 | -44.63387 | 2026-07-31 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3574de59-3728-3709-a312-99721c6774f7 | -11.82291 | -45.60596 | 2026-07-31 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 789fe7b4-1a3b-3d9a-a791-1b49e352c1cc | -16.39895 | -53.33611 | 2026-07-31 03:55:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 517b4514-1def-34a3-8fe5-628d898e447c | -14.83372 | -48.52044 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2601972a-ed7b-380d-885a-ad27df426295 | -13.65619 | -39.18508 | 2026-07-31 03:55:00 | NOAA-20 | NILO PEÇANHA | BAHIA | Brasil | 2922607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| b98ad1d3-9955-3032-91a5-4349f8643d90 | -14.06782 | -46.22371 | 2026-07-31 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b15d7670-a973-3d99-8845-5036991c36a0 | -14.35826 | -48.04296 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40000b6f-e7a3-3084-9743-389d0a6d9333 | -12.85225 | -44.39182 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1e52e08f-b69b-3b75-9088-289c3f62aab3 | -15.81595 | -41.89856 | 2026-07-31 03:55:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d47f027-671f-304e-a44a-c8585d832188 | -11.82941 | -45.59677 | 2026-07-31 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61a8c331-0293-3d3e-87c1-b1940f296904 | -14.38497 | -48.07027 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f3f117dd-f699-38ea-867a-739cadd20a36 | -12.58736 | -44.62741 | 2026-07-31 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 523fd4ca-0e74-349f-b611-1a1a73abf59c | -12.03747 | -40.67487 | 2026-07-31 03:55:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3084de91-f6e2-3c00-a29d-ca09c7151254 | -14.07249 | -46.22471 | 2026-07-31 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99dc25d3-639b-3a18-89d7-044e32be3bf7 | -11.83103 | -45.59962 | 2026-07-31 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56d3ac8e-d2ed-361b-a5c8-29629ace9e7c | -17.53222 | -45.30371 | 2026-07-31 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0701a512-faa2-344f-85f1-7c38c4c9dedf | -14.39283 | -48.05848 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a41fc92-f8a0-3aaf-87c0-1ec6b6d4acbf | -16.39738 | -53.3428 | 2026-07-31 03:55:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 126dd876-2b48-39aa-a566-24266ea991b6 | -12.19892 | -47.97558 | 2026-07-31 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4421e51-6394-3373-91c6-8d8973aca228 | -14.39738 | -48.06626 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| be07e2f1-d005-3833-87b8-5f5d63b8e113 | -14.36348 | -48.04414 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac5e2eaa-bdc6-3055-bfff-f2a33bb2a3c7 | -12.60313 | -44.63912 | 2026-07-31 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 21574262-f0c7-3374-992e-762b55dbf5e7 | -14.38151 | -48.0636 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bb7e869c-9325-3934-9eeb-23b7540fb38d | -19.16322 | -40.94798 | 2026-07-31 03:55:00 | NOAA-20 | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| aeb28dba-e6ee-3be6-9f06-ef08120d7dd7 | -12.33879 | -48.22211 | 2026-07-31 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a31fe69-b000-38f3-aefc-bf5578396d86 | -15.50878 | -47.82145 | 2026-07-31 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 885a0b66-d5af-3129-87be-f0cad90191fe | -16.10084 | -47.91146 | 2026-07-31 03:55:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ee318f6-d4b0-3cf9-8752-e2bfe69ce6e4 | -14.89962 | -39.52599 | 2026-07-31 03:55:00 | NOAA-20 | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c6169f75-52f4-30d1-8efa-2f2c650161a3 | -14.23467 | -47.48574 | 2026-07-31 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 94bfc886-572b-3747-ac7b-0d3c3c123975 | -14.38012 | -48.07071 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7e2e2029-d244-3c1f-baea-359c1cfb6851 | -14.39584 | -48.07061 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b2620d82-c38f-3786-bb50-85f9c6fd0a97 | -14.38583 | -48.06947 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ca994c8b-e57d-3c68-960d-86977755a9ed | -12.45478 | -43.53155 | 2026-07-31 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3b886434-000e-3409-a71b-9f03afe0a45f | -17.53406 | -45.30862 | 2026-07-31 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 758c3275-baaf-393d-a4ec-4b06670e65a0 | -16.55941 | -49.05432 | 2026-07-31 03:55:00 | NOAA-20 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4ab2ed5-2035-3aa8-b371-9075d6576116 | -13.28854 | -43.10491 | 2026-07-31 03:55:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3ec2f73b-0eef-3cc4-851b-258641e234d4 | -14.37924 | -48.07156 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eda86046-0af6-303f-b57f-d1ff4268d994 | -12.59169 | -44.62824 | 2026-07-31 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49d21271-1e56-32de-ab20-f4702efb6fd4 | -14.3872 | -48.06243 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d16ddbaf-640f-34fd-8577-56cef9245236 | -12.61944 | -44.59841 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec527a94-a524-3e2c-b6a2-ba401015f54b | -11.82759 | -45.60685 | 2026-07-31 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e23f471-ffaf-3c06-aab5-6127ed65a0a4 | -14.83139 | -48.53222 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57ab1292-d65c-3743-a93d-b7d7b90dec2a | -16.32997 | -47.56513 | 2026-07-31 03:55:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d29b539-4350-38f6-b768-7ced36d044df | -11.4066 | -46.85579 | 2026-07-31 03:55:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07ddbbc1-a96d-3c52-8153-4fff2c6b7ea2 | -17.53146 | -45.30765 | 2026-07-31 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ad9c608-686a-3a04-92ca-5e755d89b761 | -12.62706 | -44.63046 | 2026-07-31 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f8e7320-3756-3e71-a079-3afb13b9b8e1 | -12.19962 | -47.97194 | 2026-07-31 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d30b908e-881d-3e5d-9f70-38cd9b0b66a1 | -15.54036 | -39.10919 | 2026-07-31 03:55:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a7f5063b-7054-351b-87f2-51b0d88c8577 | -14.83136 | -48.51588 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9911be95-2f2f-3596-9e6e-5321a879460e | -14.05381 | -46.22071 | 2026-07-31 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c5cd362-7e5a-3e59-8de7-d867317ee12f | -15.81666 | -41.89439 | 2026-07-31 03:55:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06df4e98-6e60-305e-95ed-61feb3af33a7 | -14.36458 | -48.03861 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c80c5094-011b-3699-98ef-a48458497af0 | -16.33149 | -47.56504 | 2026-07-31 03:55:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57af3b98-fc3c-374e-a226-40fac3976672 | -16.39857 | -53.3435 | 2026-07-31 03:55:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b5f991b-833a-3e7c-b13f-cca5ed19ccf9 | -12.58814 | -44.62313 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51eff915-f298-3f2e-aaa4-f5f9b8a8e209 | -14.39655 | -48.06712 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2987d1f3-1c31-3402-b030-77ed3a84df7c | -14.38198 | -48.05809 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdc44d18-b47f-31d1-8bda-7c660e56d369 | -14.20962 | -44.10802 | 2026-07-31 03:55:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d9247c0-4d36-3b05-b0a3-a28e515022be | -10.89603 | -45.20046 | 2026-07-31 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31e78951-480a-3d45-8946-602af554672c | -12.60746 | -44.63992 | 2026-07-31 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 370f0d1a-5933-30d3-a3a0-c000459d42a5 | -18.36475 | -46.51639 | 2026-07-31 03:55:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a8879c2-410d-3223-9d0e-53636d84ae56 | -11.40594 | -41.80199 | 2026-07-31 03:55:00 | NOAA-20 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aab61a8e-e380-32ac-85ca-7d7a389c6564 | -13.28941 | -43.09996 | 2026-07-31 03:55:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 279a1101-0fbc-36d7-9a06-19dcb6a7c2c3 | -14.3608 | -48.05777 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae71f566-c3ae-3321-b5a7-3748ff83f417 | -19.21904 | -41.34302 | 2026-07-31 03:55:00 | NOAA-20 | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 256d9e98-d00b-358b-9160-9cc9ed0dda89 | -18.12344 | -44.63955 | 2026-07-31 03:55:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 75bc08ff-016d-31bb-9573-ff97f79274fe | -11.90112 | -43.44457 | 2026-07-31 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6737ed60-4e4b-311f-92ad-fb90e7bc743c | -12.61765 | -44.63306 | 2026-07-31 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f95a8ea-a207-34a9-a752-8aa3e3395692 | -12.61513 | -44.59755 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98915730-e4fe-3b8d-9ed7-9c607eb8807f | -14.38274 | -48.05729 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f75e5518-cc24-300d-afb4-410fa50dba64 | -12.59912 | -44.61195 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 453be0d5-f556-3c13-8146-b89afadb7b34 | -14.39889 | -48.02856 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 704a5f2e-a231-3d60-bfc5-937e1bfcf3ed | -15.60994 | -41.39674 | 2026-07-31 03:55:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4aef2b88-43c3-34af-aa89-51d5b8717002 | -12.8515 | -44.3959 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9b11d0fd-777f-34aa-9567-4ba6610b5c5b | -11.83008 | -45.60464 | 2026-07-31 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7ce7552-fb92-3ec0-836d-17058fd4d6de | -14.82897 | -48.52749 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db1dbcee-528a-3d64-8bef-1f60b23af380 | -14.37841 | -48.07564 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6fd9371b-cd72-35c4-bfcb-0ee919b74e5f | -14.39159 | -48.06794 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ce8e31aa-dd45-3d96-aa98-b01ed8664293 | -14.37573 | -48.03738 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1170bdb-0474-3b8b-8e5f-d8aa31e9b59b | -12.59325 | -44.61964 | 2026-07-31 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72f79408-ba1e-32dd-95b2-42a86375ddd4 | -13.95626 | -49.14851 | 2026-07-31 03:55:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30034675-6528-3cd7-bcd2-54cec6a26637 | -14.05849 | -46.22168 | 2026-07-31 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a38dba5-186b-3e68-aa06-1bbc38f61319 | -14.40326 | -48.03393 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6f60b86-858f-3433-ba1d-1e109b33957a | -12.60823 | -44.63567 | 2026-07-31 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3f0103ff-ad26-32d2-a225-5b9e92d05ee7 | -14.83213 | -48.52847 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f03ce20-7e7b-33a2-bc38-84800c460677 | -11.82541 | -45.60375 | 2026-07-31 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ef53955-4056-3bec-a35b-130ae470a5fa | -14.0688 | -46.21849 | 2026-07-31 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e6bac9a-4f69-3b75-a10f-6ee45c64291b | -10.90067 | -45.20125 | 2026-07-31 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69ebb2b4-1007-3945-9cae-1e9ae61d37b7 | -14.40647 | -48.04503 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa316705-d530-3bf2-a00f-f3b7345df581 | -17.53064 | -45.30383 | 2026-07-31 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e7fc9dec-97bb-37c4-8529-b6b375ee68fa | -12.38184 | -40.39363 | 2026-07-31 03:55:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ad5428ec-91c5-328c-9c3a-2bd9273301eb | -14.38336 | -48.05414 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c26773e1-ea38-3dda-90c5-406be850bacc | -14.36989 | -48.03931 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad7fe520-1930-3a88-b534-2d9f4e4ec4fd | -14.40396 | -48.03049 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 628055e6-1687-3af7-a29e-19172ae59943 | -12.62349 | -44.62544 | 2026-07-31 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee92292c-ba4b-34df-95f4-f03e2f6db230 | -14.38569 | -48.06674 | 2026-07-31 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bd3549f0-4993-38ac-a5c4-7835a23faa5f | -16.70061 | -39.7166 | 2026-07-31 03:55:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5cd4362a-f704-3139-a9fa-927b751c13b6 | -12.61256 | -44.63646 | 2026-07-31 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README6.md)
