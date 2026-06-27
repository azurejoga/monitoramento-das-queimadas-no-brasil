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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cb8e8af-5a72-38f2-b2c2-d612091c65eb | -7.73809 | -44.18439 | 2026-06-27 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 3062c532-3ba3-3ff9-aac9-c805b3346f54 | -7.75463 | -44.61716 | 2026-06-27 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d61a1276-9476-37c3-9a7e-269db33071b4 | -8.49252 | -44.73856 | 2026-06-27 03:36:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cb02767-8d01-395c-9534-780d82197479 | -6.9998 | -42.76709 | 2026-06-27 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 19878feb-4d74-3f02-9144-fffb3fb85554 | -5.7824 | -45.06383 | 2026-06-27 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b9860baf-d121-386d-ab51-0617d895fe49 | -6.97207 | -42.89384 | 2026-06-27 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5c6bf3d5-881f-323d-8a9c-02204bd1277a | -5.77229 | -45.06277 | 2026-06-27 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ce56c411-586f-3323-b384-18f24bcbe259 | -7.74528 | -44.17769 | 2026-06-27 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5aaab1e7-2fc9-38f3-9a7e-96bf5e7d7f6f | -5.76887 | -45.06711 | 2026-06-27 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 044bf024-20fa-34e2-abb4-e90be5dcee44 | -5.78148 | -45.06892 | 2026-06-27 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| a05fc26a-f3ae-3533-b3c3-ac4ad549524c | -7.74457 | -44.1815 | 2026-06-27 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c098bc65-1c0d-34c6-81c9-f877c7201d21 | -6.98219 | -42.89901 | 2026-06-27 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b97285f1-daec-399d-a895-c39b74ef8801 | -7.73819 | -44.17752 | 2026-06-27 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 1d32a4bd-5e51-3886-b2c3-e078e5d4e748 | -8.49172 | -44.74289 | 2026-06-27 03:36:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da680b19-96a9-3157-94a1-aa53bfbdd8c3 | -6.98338 | -42.89225 | 2026-06-27 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c24ab9c9-1d1a-3930-b3a2-94c4423c22f7 | -13.94051 | -47.33346 | 2026-06-27 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa365935-c689-3fdb-8494-d4767e6eae59 | -9.06487 | -44.75122 | 2026-06-27 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6ffb476-5312-3657-b8cd-39bf0a58846f | -13.94571 | -47.33995 | 2026-06-27 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3fc1d5f-2183-3e70-bbd1-e1fa81768722 | -14.8513 | -48.14561 | 2026-06-27 03:38:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2c129f7-7c93-3877-8146-40eced6d8854 | -12.82869 | -44.35754 | 2026-06-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1d392c1d-6433-3a7f-bc05-c2a121b58b87 | -10.36169 | -47.33754 | 2026-06-27 03:38:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16208ce4-677a-3258-949c-930481701467 | -14.70014 | -46.14424 | 2026-06-27 03:38:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9aef584d-dd95-34cc-b543-a06f2e5483a6 | -8.67896 | -47.85044 | 2026-06-27 03:38:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7572ac8e-c3fe-3941-a98d-64bbd1b6ee27 | -15.59264 | -46.80766 | 2026-06-27 03:38:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c132010-8c2c-35e5-ad6f-b8f4fcc9cbd0 | -15.5858 | -46.81092 | 2026-06-27 03:38:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e9522b7-6ec8-3e53-91fe-6757ea11419f | -12.83402 | -44.35852 | 2026-06-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b96e5dd9-023a-3c96-abf5-e1042aa6beec | -9.06828 | -44.76504 | 2026-06-27 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2b2f598-59e0-30a9-97db-fa7913c1caa6 | -12.44785 | -44.75595 | 2026-06-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 950edf4a-e27b-3cc3-ab63-d4d578109efa | -12.832 | -44.36885 | 2026-06-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 92be563a-54d2-3613-a95f-4aef8e869597 | -12.83732 | -44.36988 | 2026-06-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 690b7dba-c9cb-3a79-b6d4-3f3e13f9a631 | -12.82473 | -44.34961 | 2026-06-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| e09ae0b8-2502-303d-b5b3-0f00628fbc31 | -9.05906 | -44.75009 | 2026-06-27 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e11558da-4457-33f2-8479-db52872801a0 | -13.94346 | -47.33649 | 2026-06-27 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d975576c-64cf-36c6-9ad7-f2d0895eaed6 | -9.07407 | -44.76629 | 2026-06-27 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56c6c920-8c07-37d9-846c-58c8836e875e | -13.94851 | -47.34348 | 2026-06-27 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce6ed7ba-e883-33a9-a18e-10964c96cb75 | -12.83469 | -44.35508 | 2026-06-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 122c1020-2161-32b7-85c7-7e1dce0e3a46 | -12.82607 | -44.34277 | 2026-06-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| f0ba1f6d-f6bd-3a69-a85b-515b102c8e36 | -14.63722 | -39.52364 | 2026-06-27 03:38:00 | NOAA-21 | ITAJUÍPE | BAHIA | Brasil | 2915502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 59f67ed8-f86a-326a-b33c-a591246cca0a | -12.8254 | -44.34619 | 2026-06-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 199e88d4-58ae-3cb0-a531-86ed054c826c | -9.07987 | -44.76754 | 2026-06-27 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe1433b7-6bdc-351a-a07b-e8dc7a34f043 | -11.78301 | -46.44127 | 2026-06-27 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab032f15-8703-3a7d-99dc-73920fd94cb0 | -12.83267 | -44.36541 | 2026-06-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 05414218-6598-3ce9-9521-0be67336f5b8 | -14.69848 | -46.1524 | 2026-06-27 03:38:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a52f749d-54ad-3b81-b790-00eda22c3c5e | -11.92445 | -43.927 | 2026-06-27 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e185a5cd-f53e-3ce7-a4ba-00a9de0ca07b | -9.08068 | -44.76325 | 2026-06-27 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2814e856-2b9f-30c9-806f-fdbb8074d3a7 | -10.35511 | -47.33586 | 2026-06-27 03:38:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 232e41bf-1198-3b1a-b2e3-dfda14b9cb1d | -11.78406 | -46.43607 | 2026-06-27 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c7f3371-1628-33fc-a222-01d762b7859e | -14.84476 | -48.14462 | 2026-06-27 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8cbea493-7b29-3976-a547-266c349c0124 | -12.83138 | -44.3438 | 2026-06-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| ea634bfe-ba3d-3b53-b39d-1319c0c2a891 | -12.83071 | -44.34724 | 2026-06-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| e7fccb3b-e3df-34a8-ba36-99ae9b7fda08 | -15.59172 | -46.81202 | 2026-06-27 03:38:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6f54cfcb-337f-386e-80b3-db0c5b7ad071 | -10.35838 | -47.33529 | 2026-06-27 03:38:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ef3955aa-1dbf-3054-ad49-eec0f0b65b81 | -14.69932 | -46.1483 | 2026-06-27 03:38:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6f981d9-0a13-32f8-b58d-f0539f224b65 | -11.92511 | -43.92357 | 2026-06-27 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29bf91f9-a8cd-37d7-823b-bd6f54342e21 | -12.83004 | -44.35067 | 2026-06-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 768a22da-d71a-3225-8eab-8e6689995593 | -12.82936 | -44.3541 | 2026-06-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 9d8e1c04-b3e0-3a46-ad49-601f6a0af88d | -12.83334 | -44.36198 | 2026-06-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fb27d312-9326-34c7-9b3b-7ab324f0388b | -12.4462 | -58.5023 | 2026-06-27 03:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 1938b9ee-9d62-38b6-b583-6f1f8fa10116 | -12.4654 | -58.481 | 2026-06-27 03:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 29f31470-f146-3f83-bcfe-e36361190ef9 | -12.6236 | -57.8926 | 2026-06-27 03:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 737b5844-69a0-3313-b1bf-d5ea2eeb01cc | -5.7758 | -45.0599 | 2026-06-27 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 211a435f-d53a-3838-9455-6b8506401761 | -12.8359 | -44.3422 | 2026-06-27 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 6f02db85-e2b3-3205-8c5c-81e5678ca179 | -12.6046 | -57.8942 | 2026-06-27 03:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 402af264-6517-31c2-9932-4618a3c75fba | -12.4651 | -58.5009 | 2026-06-27 03:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 63a77f90-5128-3e9b-80f7-8633d9754bbc | -12.4651 | -58.5009 | 2026-06-27 03:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 98fc02ff-1199-3061-8cb8-2764a3a081b5 | -12.6236 | -57.8926 | 2026-06-27 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| c5af152c-eeef-3777-87d1-0e397c355623 | -5.7758 | -45.0599 | 2026-06-27 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| b0f57597-1c4f-3cd4-8774-5fa7aef9a864 | -12.4654 | -58.481 | 2026-06-27 03:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 7506dc48-6fa9-32bf-b0c6-e50dba152d06 | -12.6046 | -57.8942 | 2026-06-27 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| bc935347-8169-3136-acdb-322ee4471bdf | -10.6195 | -50.2038 | 2026-06-27 03:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| a57386c3-fe6d-38b9-be94-24d062f7a884 | -10.6385 | -50.2018 | 2026-06-27 03:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 02ca4011-cf61-390e-ac98-d7de198b32f0 | -12.8359 | -44.3422 | 2026-06-27 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 58450700-d562-37e9-b248-fa497f37ba4e | -14.8694 | -54.5388 | 2026-06-27 03:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 3384a01c-1867-377e-a07d-3a44a0a03908 | -10.6192 | -50.2252 | 2026-06-27 04:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 388db053-0987-3289-8564-108206f76950 | -12.6236 | -57.8926 | 2026-06-27 04:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 3e19cbb4-46c7-3c21-9f30-f5f1c094942c | -12.4651 | -58.5009 | 2026-06-27 04:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 2c2615d2-7d97-3fe9-a9ce-d926f84a0d5a | -12.4462 | -58.5023 | 2026-06-27 04:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 1511cf3f-48d0-3f6c-8bb8-a5c482e4cf43 | -12.4654 | -58.481 | 2026-06-27 04:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| aba689f7-3e4e-30fa-8c77-01dfc8d0623e | -14.8694 | -54.5388 | 2026-06-27 04:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 66544b8e-357c-32a3-89c9-aca1a03c257f | -12.4464 | -58.4825 | 2026-06-27 04:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| acfb8f49-fa6b-326c-9a9f-6de5d3757eca | -12.6046 | -57.8942 | 2026-06-27 04:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 50.5 |
| b94ab0a2-ecfe-3758-99e5-d1c32e96c1c0 | -12.4654 | -58.481 | 2026-06-27 04:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| e454f585-93cd-3a22-8536-719ba4047d2e | -12.4462 | -58.5023 | 2026-06-27 04:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 44295539-0ecf-3814-8873-619afdd2e3da | -12.4464 | -58.4825 | 2026-06-27 04:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 43.1 |
| ef55b5fb-adf7-38d7-96c3-2110f36ca0c6 | -12.6046 | -57.8942 | 2026-06-27 04:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 44.7 |
| fd531518-d10e-3396-a103-c66ac2e5990f | -12.6236 | -57.8926 | 2026-06-27 04:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 2c580184-8805-3811-93a4-61c302f80404 | -5.7758 | -45.0599 | 2026-06-27 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 487767e1-48c3-3a31-8f49-6702a990cd2e | -12.4651 | -58.5009 | 2026-06-27 04:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 749297db-5caf-3802-8aa3-23d4bc445d71 | -3.86927 | -42.96942 | 2026-06-27 04:10:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| f4514be1-c18f-3372-ba6f-b9ffe50681a0 | -4.66003 | -43.22084 | 2026-06-27 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 697391b9-db9a-3c7e-be75-d226348e7344 | -5.32577 | -44.68989 | 2026-06-27 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fffa9db5-681d-39ff-8f0d-14e0f2a16c7e | -5.32494 | -44.69502 | 2026-06-27 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ebed96ca-2f62-312d-8fd3-fd0b1416626e | -5.32095 | -44.69439 | 2026-06-27 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f78c30e2-ab47-3aad-a3b8-d7ec8143c38c | -4.2783 | -48.36728 | 2026-06-27 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 263e1230-8de9-35b5-840b-983a05f7d027 | -3.86559 | -42.96882 | 2026-06-27 04:10:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 459c79dc-6c8a-38ca-836b-be7e336d4593 | -5.52112 | -37.486 | 2026-06-27 04:10:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e64dd981-5ce2-367a-a710-e3fdd54b8a3b | -4.14468 | -43.65874 | 2026-06-27 04:10:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23965207-bb2b-3f60-a7c0-6950878882f4 | -5.12962 | -42.88064 | 2026-06-27 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf318602-654f-3bf4-b53a-8aedc16f34f8 | -3.87237 | -42.96825 | 2026-06-27 04:10:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| dc9e75fd-791e-3778-b5b7-6591cb5e4f9e | -5.32331 | -44.6912 | 2026-06-27 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README9.md)
