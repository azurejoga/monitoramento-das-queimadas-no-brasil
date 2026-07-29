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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ea73a71-5f17-32f8-a0dc-a1f7bb2b1a71 | -10.36044 | -49.74881 | 2026-07-29 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b3c2d32c-ee6c-3a03-a44d-f943ac0766cd | -7.35787 | -45.83889 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b08c0820-ea13-3036-ac74-da610c731118 | -7.35869 | -45.83252 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| e7ed9d0f-badd-3a6a-8566-7962e7fc7c55 | -9.73263 | -62.37706 | 2026-07-29 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b473bc18-d00b-3b6b-bf48-4a0e3fff1ae8 | -11.61903 | -50.338 | 2026-07-29 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f51fe620-43ea-3bc7-b63e-e386620790f7 | -7.34224 | -45.8504 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a23184a3-6439-32c8-bfba-21c5ffb6ece0 | -7.34921 | -45.85109 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fce47d7f-4e89-3909-a33f-01e672a2580c | -8.92947 | -64.9949 | 2026-07-29 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 236e5adc-e68c-37c3-877b-17a7d60e1268 | -8.4433 | -51.5503 | 2026-07-29 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95746ebb-511b-3b2f-9664-96f3740ae671 | -12.15086 | -48.95284 | 2026-07-29 05:18:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48119ce6-5f36-3787-98ef-0e0b3bc0cd1d | -10.36285 | -49.75215 | 2026-07-29 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7b2ae16-05c5-3d85-9eae-09da7a367fcd | -8.44892 | -51.54548 | 2026-07-29 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7cb4868-098d-3d89-830d-7899850ea88d | -8.81912 | -66.75318 | 2026-07-29 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73e9c156-df8d-37d6-bcd1-2f244159c459 | -7.73019 | -47.24802 | 2026-07-29 05:18:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1d2db67-f316-3ae7-9ea9-bc878fe4bc11 | -9.19215 | -58.06625 | 2026-07-29 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00999632-399b-371e-a99c-77373f1a3200 | -9.10182 | -50.60924 | 2026-07-29 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6588891a-0231-3c7b-b4e9-5c8780faed16 | -11.18107 | -49.93454 | 2026-07-29 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 955674e3-0ee6-3fea-992e-bd3fccb22b1d | -10.33746 | -49.72485 | 2026-07-29 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6a3c82c3-e728-3a52-8b9c-a5b66c6ecf2e | -9.47291 | -63.28166 | 2026-07-29 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7237d522-6e1e-3cf1-b9f8-350c4eb80964 | -11.53107 | -47.56411 | 2026-07-29 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d5b9215b-2c55-380f-b4dd-ae8634b077d8 | -11.09973 | -54.80823 | 2026-07-29 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6af3dc16-0b4e-3da4-a673-820d6934a86d | -7.34308 | -45.84393 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 83e3287f-3485-3a4b-b313-21600ec3370a | -7.34392 | -45.83741 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 0451a113-71e0-39d6-8922-98df2616d1b9 | -7.35089 | -45.83821 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 4cb80f96-70d3-3d6c-a6ec-de57e178127a | -7.34957 | -45.84268 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 82cea091-086d-355e-8382-6a5aa74a569e | -7.35734 | -45.83697 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e53af832-d520-3855-b39d-04a0af6e5e91 | -10.3219 | -49.71076 | 2026-07-29 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9cb7dfd5-d328-3b8e-ac96-8c9644527005 | -12.15005 | -48.95272 | 2026-07-29 05:18:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9ca338a-5cc3-395a-a95f-56eb1f93b026 | -9.50049 | -66.71712 | 2026-07-29 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a255c1df-628d-3d5b-8cf5-de26d6b0fee3 | -10.36851 | -49.75292 | 2026-07-29 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed5280af-a388-3845-a8b4-ea7b3045f198 | -7.90289 | -48.28424 | 2026-07-29 05:18:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 051859f0-9045-392a-9fe0-284a592e4238 | -8.83655 | -65.05259 | 2026-07-29 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5e75713-a390-3f8d-a829-7bf397eaba25 | -11.1898 | -54.04102 | 2026-07-29 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3512e777-57bf-3989-bf1d-42b095b744d6 | -7.34141 | -45.85681 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4565d76a-b795-3a3c-b708-78dfc3166dfc | -10.34313 | -49.72564 | 2026-07-29 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 870c9870-821b-35b0-bb56-6237b92c043c | -9.40775 | -55.97502 | 2026-07-29 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01a0c84e-ece6-38b0-9418-3e040c4a653d | -7.34181 | -45.8484 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 60831c8e-9277-37eb-81c5-b822fb3816d6 | -11.55699 | -47.57142 | 2026-07-29 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13762a67-ab19-3629-bf1e-67fb2e169945 | -10.36564 | -49.7535 | 2026-07-29 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54153218-45d8-39e2-a5c6-2b5ae629fa12 | -8.83368 | -65.04432 | 2026-07-29 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4e27935-1a6b-369f-8216-a41e99106112 | -10.35718 | -49.75138 | 2026-07-29 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4cb6bfc8-6146-37d0-aa57-746ea235c1bf | -7.35813 | -45.83058 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 69060334-39d6-386b-8baa-46587cf03cf6 | -9.09614 | -50.6118 | 2026-07-29 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88948dfc-89df-33f0-9c14-da543f6842c6 | -8.8229 | -66.7589 | 2026-07-29 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 690e5aa6-71d5-30a3-97ad-ebac16ba0234 | -7.72955 | -47.2531 | 2026-07-29 05:18:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99f4fbfe-c8ec-311d-8497-3e1204726b78 | -10.35524 | -49.74413 | 2026-07-29 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d6455df6-69b0-3609-b009-d4fbeb3e4401 | -10.35152 | -49.75061 | 2026-07-29 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8cea0c2c-f2b1-387e-9dbc-3f4b562e1d3a | -7.90554 | -48.27858 | 2026-07-29 05:18:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f023cde5-d2dc-3e94-9fcd-7f72ac68830a | -7.33445 | -45.85607 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| cd44585a-aedf-3a85-bf5e-5ec76c3902f3 | -8.44404 | -51.54475 | 2026-07-29 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f91bc332-2172-3598-ab9c-a0ebf5f455db | -11.74945 | -46.73216 | 2026-07-29 05:18:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0167a1d0-efe5-3d7d-95bd-5d5200ba7a98 | -10.36334 | -49.74826 | 2026-07-29 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf2bab80-fb9f-3b43-8840-8388310d1351 | -8.44818 | -51.55104 | 2026-07-29 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fe4cb42-06de-3566-b0ff-0e88c5fe1bd0 | -8.81826 | -66.75806 | 2026-07-29 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f439df04-c1af-3882-8dc3-b613aeea79bc | -7.34261 | -45.84189 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d5946b3c-2bb1-3c8e-b4b2-9d84c289f6e8 | -9.91953 | -67.04707 | 2026-07-29 05:18:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88a1246e-7cd0-3813-8e9d-e962fa5f5643 | -11.56423 | -47.56661 | 2026-07-29 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a21f38fb-5b55-3f3e-ad66-7f1b84079350 | -11.18059 | -49.93843 | 2026-07-29 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f50127d7-0a05-3dc2-b65f-359bcc0b4e41 | -10.2384 | -58.51498 | 2026-07-29 05:18:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a268ff4-f5c1-362c-bf6a-4c67d869dc0e | -10.08973 | -59.0393 | 2026-07-29 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ebf7b63-56e1-3596-8198-5571f66df9db | -9.18877 | -58.06573 | 2026-07-29 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 679b90a6-4b9e-3924-bc2e-2fe587647521 | -7.90349 | -48.27972 | 2026-07-29 05:18:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 09891e1d-eae8-38f8-b617-b87e96895b3c | -10.35768 | -49.74748 | 2026-07-29 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5f5fd886-9bb6-32f6-87b8-30d5e8fe9e66 | -8.83846 | -65.04125 | 2026-07-29 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04b83134-1e54-3a1e-9a7e-c4ff7babcc60 | -12.31419 | -46.75246 | 2026-07-29 05:18:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73143f3b-fcb5-3356-9c2e-baaf28234955 | -7.34878 | -45.84914 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| aba02d57-2b42-3038-b0e4-06c436b10d50 | -9.61163 | -47.76406 | 2026-07-29 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 56fa2b3f-460c-39ff-8ccc-7e8206a8c62a | -7.35172 | -45.83176 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| f0fea10d-ccce-3b42-830f-b3df202f672a | -10.24055 | -58.51492 | 2026-07-29 05:18:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b1dbff0-40a3-363d-8453-00b673c48239 | -7.34102 | -45.85486 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 2e0fd715-18d0-3dda-bffd-619730237897 | -11.53163 | -47.55914 | 2026-07-29 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 71a9dc3a-5ed9-3ab4-bde5-a59878671b50 | -9.4792 | -57.32304 | 2026-07-29 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc5bee24-178d-3c5f-a63b-512fff1a6430 | -7.90497 | -48.28307 | 2026-07-29 05:18:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45c8d3a5-d608-3365-b4eb-a6a3a164c594 | -9.1014 | -50.61259 | 2026-07-29 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eac51efa-27bf-3756-84af-59f194b00a80 | -7.35117 | -45.82973 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f166833a-b237-321c-95c4-084dcfbd245f | -9.61097 | -47.76945 | 2026-07-29 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 12420911-e108-3994-bc47-d701b41958dc | -11.18394 | -49.93579 | 2026-07-29 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c7a4da11-e7db-3480-b0dc-b0ae04b50466 | -11.61858 | -50.34171 | 2026-07-29 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55aa3165-e2c5-3e8a-9a46-05c1a0a1dc97 | -9.48268 | -57.32358 | 2026-07-29 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1961db54-466c-3930-b7f0-7e1ec30e8e10 | -10.3543 | -49.75193 | 2026-07-29 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6f69ce91-1fc9-3feb-8d76-7a0add03817e | -12.15063 | -48.9478 | 2026-07-29 05:18:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 528c2bce-894b-32e7-a0ff-0a7a5ceaf717 | -7.7281 | -47.25114 | 2026-07-29 05:18:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04c14bfb-ce79-3b94-b2e2-3dc097baf633 | -11.74881 | -46.73834 | 2026-07-29 05:18:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a06f827e-106b-3822-adaf-c9925e1f1592 | -11.74951 | -46.73467 | 2026-07-29 05:18:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 70331f7b-bf01-3dcd-88bf-bd71564d1868 | -7.35037 | -45.83624 | 2026-07-29 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 282bd799-2bc2-3aa6-9e8b-d533004152d7 | -12.1514 | -48.94793 | 2026-07-29 05:18:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bc7b76b-ac44-3ec3-ab0b-798110392c06 | -10.3525 | -49.74282 | 2026-07-29 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 29e122b7-bc08-39bf-97dd-8f8c37403e04 | -10.32757 | -49.71155 | 2026-07-29 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 19676ea7-ad1a-35fd-b681-51a73c6c6ef1 | -8.82376 | -66.75401 | 2026-07-29 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d1675a80-0b97-3c3f-85f5-26b543a8608a | -7.3413 | -45.8377 | 2026-07-29 05:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| b8812d1d-c43a-337c-a2ea-12c6d758af00 | -10.9401 | -43.0355 | 2026-07-29 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| ce613556-d8d8-3a9b-8d24-a16e700be160 | -10.9397 | -43.0593 | 2026-07-29 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 91230e4c-bff7-3639-a0a6-b11d7be308a0 | -15.40612 | -55.93513 | 2026-07-29 05:21:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43b08a45-c0be-3798-893f-3bf0e96ff1c0 | -14.3368 | -58.95474 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 282f949c-10f2-3f3b-94e0-4363cd3d016f | -13.73103 | -51.9127 | 2026-07-29 05:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e13c2225-c390-3823-b309-c6f5a64a968f | -14.01726 | -53.93799 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dee32224-fb0b-3d2d-8535-094509e97be2 | -14.29479 | -58.99858 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acc6aa2a-6575-383d-89fd-0aef7509681e | -14.00472 | -53.96399 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c027e84-5d02-385e-bc87-031f2dacb123 | -14.02068 | -53.96474 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 172ecc9a-9314-3aac-8e56-0780c41b1c49 | -14.02852 | -53.97514 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README16.md)
