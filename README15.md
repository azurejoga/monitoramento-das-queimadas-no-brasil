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
| f37d3b37-6e11-3d00-ad1d-5ffb73799dcb | -10.7023 | -47.7326 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffb4fef1-c2d5-3a35-a631-bbd2ea12b737 | -10.05529 | -46.42542 | 2026-08-23 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9a751cb3-2a61-3a7f-9116-b44396337632 | -17.59389 | -44.61386 | 2026-08-23 04:10:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a18cb03d-79f8-379e-9e6c-70c89e85d481 | -16.09173 | -48.48807 | 2026-08-23 04:10:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c18c80a-de13-3eeb-b0a7-0bcf963a1c96 | -12.25846 | -43.18784 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 70e22521-cf06-37b9-bdad-056483daa6c1 | -12.77202 | -47.1258 | 2026-08-23 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5dc3b607-5fc3-335b-a3b7-1fc456e8de2c | -17.20837 | -47.52411 | 2026-08-23 04:10:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1e4ae1c-ab89-3957-aade-978f99782266 | -16.57045 | -51.62954 | 2026-08-23 04:10:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4b149c1d-6f47-3eab-bc32-d08cd8ad7d7b | -14.14617 | -48.05342 | 2026-08-23 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f09c9b2-7454-33ff-a6e9-796984134658 | -13.66567 | -51.85259 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 76a65681-a993-39f9-9809-435c9662d8a3 | -12.29045 | -43.15694 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4e45dcb3-34d8-39f0-9b96-96cba7562a81 | -11.27712 | -50.74202 | 2026-08-23 04:10:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf7241f0-7ce3-39e2-88fc-b12354bda207 | -17.71554 | -43.50243 | 2026-08-23 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcc6b96c-0d56-3800-8ed1-3d66a39b2460 | -10.71315 | -47.74205 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6b7b9b0-93b0-32f7-9e60-b227a9dc0ce5 | -14.48568 | -51.81558 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7ce93cdb-17bf-34a0-9b82-8cf3a7fa9cf8 | -13.22637 | -51.44668 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc922b5f-bb37-3761-9467-d4abdb29d21e | -12.84151 | -48.47861 | 2026-08-23 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae3fc9a0-d7f8-3c81-874b-5da9ac5f8d05 | -14.99877 | -52.6944 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 316862e6-6de7-39dc-b111-d0baf056dd5f | -14.95371 | -52.65051 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 21c160a8-8877-3d89-aa0f-b2df738ab3b2 | -14.14916 | -48.05688 | 2026-08-23 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8129ed90-4ef0-33da-8626-354a97edc664 | -13.66529 | -51.85851 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59e3123e-c363-38ee-accf-4a2a43e8cc4f | -8.52605 | -55.34534 | 2026-08-23 04:10:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd77e9ce-dcd4-34e5-b1a2-05b4663f5966 | -15.32761 | -46.08305 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77e46ec7-73c4-3e65-9d43-371ffa54bb3a | -14.14528 | -48.05606 | 2026-08-23 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88225a4b-b903-3ed0-a67a-b33a518bf105 | -11.14282 | -46.18 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5311bff-663e-3cbf-aa10-6767197cb3ce | -12.73857 | -48.39754 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 32012372-7a5a-39a1-a8ff-d6cd6771b2d8 | -10.7057 | -47.737 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e865e90-ed54-35e6-a934-4a5ec367601d | -15.21187 | -52.80218 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7e24b9a-9141-3fae-a1b3-1b37c093d98d | -12.74965 | -48.38214 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6da32ae5-7fd8-3ea0-8f3e-0efca032c16a | -15.51265 | -49.83513 | 2026-08-23 04:10:00 | NOAA-21 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c323f0d0-3532-3624-9e81-231e2ae38ca2 | -8.53155 | -54.81841 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5c89bf5-3f6b-32e4-b3de-4b1f0019d15d | -17.07107 | -46.41654 | 2026-08-23 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e8859fe-c74c-3bd9-be61-43b3f17b6c2e | -16.06074 | -50.42889 | 2026-08-23 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 80039ae7-ad08-389d-ae5a-ba0565e4916f | -16.39587 | -51.33214 | 2026-08-23 04:10:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22a2b74e-a0ff-3f27-a99e-06e34af53903 | -10.55471 | -46.39362 | 2026-08-23 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| be5c4a53-c20b-3216-8f19-77002f2b362b | -13.45069 | -43.84422 | 2026-08-23 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| faf5e33d-aa84-3fcb-a95f-29398ce5df47 | -14.96661 | -52.66665 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 20bc4e27-6813-3e74-bd86-ab49c3add68a | -11.43122 | -44.53701 | 2026-08-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3be38607-a351-3457-b302-4f08cd1b9852 | -12.23807 | -43.12324 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 18d55cee-99ae-3c86-877e-397443004e4c | -13.6669 | -51.84996 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6abd87be-d71a-3fff-b469-a0e6ebfaf28c | -13.1941 | -51.42864 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 86285c2e-af47-3783-acc7-2c9fdc091b12 | -11.61498 | -50.56141 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| b716c428-85e9-34aa-b146-3b6dc2a3abbe | -10.70633 | -47.7333 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9757c3e-037f-35a4-92d2-e4a6fb4b9024 | -12.48918 | -44.77165 | 2026-08-23 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 633ba408-7b59-38db-8e45-d55ba2f1f1d4 | -8.52721 | -55.33931 | 2026-08-23 04:10:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0757a90-ebc7-3fc0-a721-90a9c81eeb18 | -17.21276 | -47.52037 | 2026-08-23 04:10:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d38c0c6-5199-3572-bea1-231d27af0063 | -13.183 | -51.42506 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 065afb6c-42fe-3f38-ac75-eed52e1ac7c1 | -12.8159 | -48.40936 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98ebe246-c1aa-37c8-9b95-8e244db663a9 | -13.16225 | -51.4269 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| b4827b9b-bbe3-37ba-904d-952655436050 | -13.19776 | -51.42795 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9c2a6dc0-2927-3bcb-add0-6cf689cdcaec | -12.65567 | -47.64489 | 2026-08-23 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23def011-99ed-3e73-93d3-4c1038e4b962 | -12.73388 | -48.40034 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6918179b-7a9d-3327-bad5-58bb68db2f87 | -16.05639 | -50.42793 | 2026-08-23 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e9af1c51-11d9-3050-a111-9a9de8ba62fe | -14.8126 | -42.40251 | 2026-08-23 04:10:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7c6732d7-ffb9-3e7b-84d8-1b24614c9fcf | -12.25515 | -43.1873 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1c53ca57-7d4a-3130-8abc-86f6c510baf0 | -10.45393 | -49.97384 | 2026-08-23 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ebe8e6d5-fce1-30c3-8064-dda09c40f0f3 | -14.9589 | -52.65141 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 25ecc076-5f71-3d7f-816f-d142cae7cdd7 | -10.68341 | -47.72178 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2386f0b2-0c8b-3d32-814c-c21c2cf5dfa9 | -14.80254 | -48.78383 | 2026-08-23 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 116e0ccd-06b2-32ee-9752-af5ab2d53019 | -10.05076 | -46.4294 | 2026-08-23 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9f275dcb-2a85-3ec5-be1a-7382e12f2529 | -15.34179 | -52.77818 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdd7d72e-3f80-3dcd-a01f-329bf8695cda | -17.4068 | -48.11731 | 2026-08-23 04:10:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9a123c3d-da0e-3942-8873-4d084e159562 | -13.16824 | -51.42218 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6740f408-2cd7-3310-b1e6-5adc391d5df1 | -8.53835 | -54.82986 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d009699-83e7-3ed9-828f-38afb7d59fd1 | -15.51688 | -49.83605 | 2026-08-23 04:10:00 | NOAA-21 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7eab6ae7-64c6-36d8-aac0-bc29f3a1fdc2 | -13.09735 | -43.34619 | 2026-08-23 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f357b48b-c101-380b-b22a-79850e5123ea | -11.55308 | -46.95038 | 2026-08-23 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0c5464e-6551-3f7a-949d-1bdde71607d8 | -13.66582 | -51.85572 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c4858914-0eb7-3df0-80a3-6c6703cb9184 | -10.0658 | -46.45541 | 2026-08-23 04:10:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ec247b4-9bfd-3a10-95c8-409b740b4ca1 | -12.22182 | -43.15983 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cd730101-9f14-3d00-8a96-4c910b041ea4 | -12.40794 | -42.90568 | 2026-08-23 04:10:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e8173f72-a2e4-342f-9c40-52736bf57fc3 | -12.83744 | -48.47785 | 2026-08-23 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2bb32d3f-f991-3177-89e1-f9efc934d8b4 | -16.06428 | -50.43425 | 2026-08-23 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d187b757-0a41-3f59-9378-acea780f3559 | -17.15968 | -46.41128 | 2026-08-23 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b91f4984-7d06-34c8-b48d-692f46ee1890 | -10.05304 | -46.41567 | 2026-08-23 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cdf35e50-7900-3fbc-9260-df281c0517c3 | -16.06345 | -50.4387 | 2026-08-23 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ad78687-d770-3705-81bd-afc515fe83cc | -13.43514 | -43.85633 | 2026-08-23 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8c1ca72a-5be6-3b4e-8f12-e8d0572d667b | -12.58589 | -47.88412 | 2026-08-23 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9cbdd3d-c509-3a6d-b5bc-4935fceca4c8 | -13.3802 | -41.32574 | 2026-08-23 04:10:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4773edca-1fe2-3e7f-9f5d-7befffbce474 | -11.35345 | -46.33499 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0576595-c5b0-3e35-af9b-cd6d1fb78db1 | -13.15674 | -42.4133 | 2026-08-23 04:10:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 598b4d34-d152-3a27-acdb-2f1ef7ab0a35 | -13.68183 | -51.84983 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b0488a70-72c3-31c5-8252-1af9cadc5fe1 | -15.5134 | -49.83109 | 2026-08-23 04:10:00 | NOAA-21 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0403de4a-eed3-3162-893e-d1ca576a5a68 | -13.10065 | -43.34673 | 2026-08-23 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9533d641-6c01-3909-bf67-a76fa7c8399c | -12.85123 | -48.47114 | 2026-08-23 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8eb500d4-c07f-37a9-b07f-d37fefb8ad42 | -10.0628 | -46.45012 | 2026-08-23 04:10:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9c11423-29ae-3aa8-bc21-00b9d592eda7 | -12.28714 | -43.17804 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ac688b01-5fc3-3fd0-94b1-13a067466f28 | -12.66651 | -42.28791 | 2026-08-23 04:10:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a6df50ac-2579-35e0-ba29-d9f59223e419 | -14.75553 | -40.86003 | 2026-08-23 04:10:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 152555bd-a137-3df8-a59c-8e3db0cc3260 | -12.28493 | -43.14883 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c661f6bd-cd56-31f1-82c7-399591e9044a | -14.34889 | -51.77478 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3e0ad55c-0653-39b1-8312-186b155fde4e | -13.16717 | -51.42786 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 12cf5f97-5f6e-395e-b45a-30f0a14d88fe | -13.29543 | -44.51955 | 2026-08-23 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bb38218-3499-3317-8079-d25f351d2b43 | -16.28765 | -48.01783 | 2026-08-23 04:10:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d22a7ee-3073-3232-9699-7bbda0647c04 | -10.8028 | -50.97017 | 2026-08-23 04:10:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31f779dc-a965-3d3e-b467-859a566664c3 | -12.58984 | -47.88482 | 2026-08-23 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08f78d87-d459-3446-8d3d-fa8472f49d67 | -13.17103 | -51.43451 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7e344ff4-aeea-348e-995a-f4e7e54044da | -17.40845 | -48.11546 | 2026-08-23 04:10:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4c6f2af-2bc8-3a2f-802a-e528d5c83ec7 | -10.46423 | -49.9705 | 2026-08-23 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6c5188d3-147c-34fc-b3d5-8d63e388579a | -14.30476 | -53.23466 | 2026-08-23 04:10:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README16.md)
