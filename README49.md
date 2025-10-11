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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd97a97f-b418-31aa-9df6-aa34cbe0d0c7 | -7.75718 | -44.71364 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7d4f3e21-3db7-3d08-826a-5008d13274d1 | -14.56857 | -45.56666 | 2025-10-11 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| db7e6af0-6487-3bc3-a6cb-48c2419a4619 | -12.50194 | -43.16219 | 2025-10-11 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2860973b-2344-33c3-839e-7415b135536d | -8.90982 | -46.00053 | 2025-10-11 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cc00f50d-e123-3926-afe1-793763972e2f | -16.72014 | -43.10692 | 2025-10-11 12:00:00 | TERRA_M-T | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| be2cb3ea-7bd7-33e0-916f-805f0570175c | -7.13919 | -43.25442 | 2025-10-11 12:00:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e1523c50-f8fb-3f44-8412-8c5852115126 | -12.44209 | -42.93508 | 2025-10-11 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 3867cba1-c8a0-31e1-90f8-6f360750c524 | -8.49411 | -46.17241 | 2025-10-11 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| a9835ce3-9423-3a5e-a36f-ec19fffe98ac | -12.90413 | -47.03207 | 2025-10-11 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| d20f6bd1-5bc1-37ab-b231-edf9553a905e | -13.84882 | -45.81411 | 2025-10-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 0ed8864b-e167-3e1e-8a5f-a8b71ef38891 | -8.16429 | -43.32 | 2025-10-11 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| e2189abd-05da-3035-95e3-84c2a7e58802 | -7.75863 | -44.70371 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0d39728a-6284-3992-b729-89176f24cf78 | -8.21361 | -43.35446 | 2025-10-11 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 8c5fb8ce-c7e3-3bc1-979a-564b3a452a14 | -14.56712 | -45.57627 | 2025-10-11 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 26c6ae46-b7a7-3ae3-8865-f867dfc46dbe | -10.93431 | -47.1657 | 2025-10-11 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| ffe60957-8cf5-3b34-a0b2-e1672f278d8d | -7.42902 | -42.97692 | 2025-10-11 12:00:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 485af71e-fed9-3d14-9b5a-233ed05ddcf1 | -13.74203 | -41.537 | 2025-10-11 12:00:00 | TERRA_M-T | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 04916335-fd1c-38d8-8a97-f446d06554d2 | -8.48668 | -46.22076 | 2025-10-11 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| a2a125d4-1ae6-30d9-9373-9562d90bff2d | -13.45513 | -47.70468 | 2025-10-11 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 67da4512-3a11-3dea-aac1-bdaceb5daa3c | -13.85805 | -45.81549 | 2025-10-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| cb076481-9e0d-3347-81c2-5394d81b2049 | -15.92772 | -47.96434 | 2025-10-11 12:00:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 360622f7-fafd-34cb-9529-9bfc3fbb53d8 | -15.22777 | -47.90565 | 2025-10-11 12:00:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 31.8 |
| a3d689a2-3010-3071-bc49-209259b38969 | -13.45183 | -42.37056 | 2025-10-11 12:00:00 | TERRA_M-T | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 3e9fe7a3-8637-3b46-8cc9-e0d7a2dbc951 | -13.26061 | -48.00531 | 2025-10-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| d1029a1b-6322-34e3-893f-106b161804b2 | -7.13798 | -45.92326 | 2025-10-11 12:00:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 4e14e1ae-8d1e-3b3f-b1ac-41f4d1e86dba | -12.84081 | -43.24517 | 2025-10-11 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| f7dc6f0f-337e-3590-9c4e-8af2dbf5c609 | -7.35104 | -45.32512 | 2025-10-11 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 2fbd560b-e7ef-3ee3-968d-0da5d1095450 | -14.9513 | -46.74131 | 2025-10-11 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| d1b1169d-f6de-34b9-a6c8-afb5b8fe817b | -7.13789 | -43.26342 | 2025-10-11 12:00:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 40.6 |
| 27046226-03ff-33a4-be24-fd94bd077fd7 | -11.78652 | -45.03606 | 2025-10-11 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c58eb473-88df-3078-91fb-808151b2cf26 | -7.86547 | -44.47465 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 11cdf6d8-a798-34d3-9a21-08b85474ef28 | -14.27037 | -45.89116 | 2025-10-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 96805157-5344-311b-82b9-bc3d67759f35 | -13.49363 | -48.11334 | 2025-10-11 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 33943d91-a9f1-38ac-acd4-c74cc41efc75 | -9.10955 | -45.03387 | 2025-10-11 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 014a1d3e-34d2-3b37-a0ed-39c59891ebe6 | -8.16644 | -39.18623 | 2025-10-11 12:00:00 | TERRA_M-T | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 36f10108-78b1-371b-a5a5-8a4c76c7f8d9 | -10.96632 | -43.0167 | 2025-10-11 12:00:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| fc9be23d-d7d3-3b64-b0a6-1c817004b563 | -11.75971 | -46.34983 | 2025-10-11 12:00:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 20c7a481-2c43-3f5c-a2df-cf4f3c204a7f | -7.6618 | -42.57966 | 2025-10-11 12:00:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 0ffa726a-a3e2-397c-a782-f7d00ad6375f | -15.29344 | -41.55317 | 2025-10-11 12:00:00 | TERRA_M-T | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| f0747fbf-5c20-3c7e-913a-0f2457085125 | -7.68072 | -42.57331 | 2025-10-11 12:00:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 991cf0fa-14ad-3579-9c69-474ff041f4cc | -7.13979 | -45.91141 | 2025-10-11 12:00:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 3d79dab9-896c-3912-b2a4-5b60318d3483 | -7.542 | -44.59878 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 11000844-0191-3fcc-86ca-c88ebd6fc896 | -15.00826 | -45.59156 | 2025-10-11 12:00:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 38fdc609-63e5-3424-a56c-add332795f6e | -8.4904 | -46.19651 | 2025-10-11 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 94392473-6e4b-3644-b073-a12777b56cdd | -7.86145 | -44.12282 | 2025-10-11 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 24773d09-d180-3d25-b06b-e797db1e3d1b | -15.4243 | -48.02848 | 2025-10-11 12:00:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 31.9 |
| fadd2f12-cbab-3276-9966-3779bc98e435 | -8.04727 | -44.1146 | 2025-10-11 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 1cf559ba-1a19-3afc-9f29-39f4c117a66e | -9.39057 | -45.80743 | 2025-10-11 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| c15453a9-56e7-39d3-a1d7-1baae5f43580 | -8.32761 | -38.09587 | 2025-10-11 12:00:00 | TERRA_M-T | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 29.6 |
| d51364c3-cc3c-39de-b9be-126b982bffed | -14.01913 | -47.05127 | 2025-10-11 12:00:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 4510ad0e-3a3c-3ebd-9a9b-8ed3da69de58 | -10.19821 | -44.60891 | 2025-10-11 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 09968e63-561d-3a16-bad0-13203fb9f4ac | -10.93629 | -47.15304 | 2025-10-11 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 771b341f-17e8-32ce-9aa2-9ca9957162d1 | -7.4303 | -42.96804 | 2025-10-11 12:00:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 6900bdb4-d0de-3cdf-95ce-dc420c2de838 | -8.19089 | -43.32382 | 2025-10-11 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.2 |
| d5c47a5c-5218-37a3-b4f2-5e88d86351d3 | -16.43882 | -46.86689 | 2025-10-11 12:00:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bef7fa02-35fe-32e5-b920-0b77f7066db0 | -9.11106 | -45.0239 | 2025-10-11 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| dd779525-b136-3edf-a3de-c4d7934df3cf | -10.51371 | -47.35498 | 2025-10-11 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| ac00238e-8f62-3cba-b2fc-43c8852477ed | -16.19486 | -41.75944 | 2025-10-11 12:00:00 | TERRA_M-T | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 1120bb02-8cf5-36e7-b5c1-63745183752f | -14.86484 | -41.71893 | 2025-10-11 12:00:00 | TERRA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 8f7c9faf-d723-31cd-9fcc-715dae47d3cd | -10.94107 | -47.92181 | 2025-10-11 12:00:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 84d5ebad-a413-3453-9245-29465d4f29f0 | -13.85656 | -45.82545 | 2025-10-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 3e35d173-63f5-3962-867d-5722ff83f232 | -7.8704 | -44.50518 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 127.0 |
| eaf66609-42ce-329a-8a56-4a174f60caf8 | -8.48854 | -46.20863 | 2025-10-11 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 83e5a3f0-6146-317d-932d-48747dde8599 | -7.61396 | -42.39552 | 2025-10-11 12:00:00 | TERRA_M-T | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 95280568-1f53-33e1-ab24-bde0ca408b4f | -12.23431 | -51.12836 | 2025-10-11 12:00:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 30.3 |
| e5402fff-4cb9-3176-807e-e9f6f01cd0e3 | -8.49227 | -46.1844 | 2025-10-11 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 9288a351-ee85-3939-8c6b-3d8189684814 | -12.77193 | -48.66088 | 2025-10-11 12:00:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 532905f5-3f78-3c83-9fe4-26165a06dba0 | -17.0293 | -40.83604 | 2025-10-11 12:00:00 | TERRA_M-T | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 098d8d62-635d-38ca-96c6-5d053def31be | -12.38909 | -42.52879 | 2025-10-11 12:00:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 34.6 |
| ffa59cfa-31fd-311a-ae7f-dfe8d41348af | -15.70731 | -46.63245 | 2025-10-11 12:00:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9d3fea94-33bf-3f5a-87be-ff4808904285 | -14.83471 | -48.48017 | 2025-10-11 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 21abff48-3184-3f53-9c66-92f4db6a0038 | -14.83611 | -47.34174 | 2025-10-11 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7b0e1029-60b0-3794-bd31-5147700afe8f | -11.88665 | -45.48585 | 2025-10-11 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ee958df8-b504-3cd6-aa50-052f12175da5 | -12.93559 | -42.30911 | 2025-10-11 12:00:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| b1a455f0-3fd7-31ad-8258-80f122c7b7f1 | -7.53254 | -44.29264 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| eca78bd4-4202-37ce-9f01-35ee1fe95ad2 | -15.46214 | -47.5347 | 2025-10-11 12:00:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 47b32f38-2dff-34f5-9b82-55aae66647f8 | -7.34132 | -45.32373 | 2025-10-11 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 8045f666-1234-3438-8137-16d1a9e361a4 | -14.27957 | -45.89268 | 2025-10-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 4588e920-4461-3a72-962b-85498514c153 | -11.77288 | -46.32932 | 2025-10-11 12:00:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| cbd82fe5-f78b-3a22-b1de-f85a57e831c3 | -7.85624 | -44.47338 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| c95cc5f8-4fbc-3099-947f-f5c15e9368e2 | -7.79733 | -44.18405 | 2025-10-11 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0a4d7625-3da7-3518-a0bd-ec1356e2eacf | -11.93856 | -44.82307 | 2025-10-11 12:00:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b2f9d05c-1a08-3f52-bbc9-fd2d5d8c5828 | -13.37891 | -47.7384 | 2025-10-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 0f01f5ff-8105-39a9-bf03-12f5cd54ea3e | -6.92674 | -43.5786 | 2025-10-11 12:00:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 2f9861e1-e74b-3397-80c1-6050cc526242 | -7.86117 | -44.50384 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 1b073764-2005-3a15-a346-2bf17a493d6a | -17.49471 | -42.75368 | 2025-10-11 12:00:00 | TERRA_M-T | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 824bbeda-9896-3563-b2ee-06ea65d485b4 | -18.09557 | -45.49681 | 2025-10-11 12:02:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| dfc4a963-676e-36c2-a5ea-310d8221879b | -20.84622 | -41.91619 | 2025-10-11 12:02:00 | TERRA_M-T | PORCIÚNCULA | RIO DE JANEIRO | Brasil | 3304102 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| a6f9e445-d68a-3884-87c6-6626fc63b80b | -17.21931 | -47.65341 | 2025-10-11 12:02:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 46e50990-6161-3ba8-b8d8-495ed27b2499 | -17.20956 | -47.65171 | 2025-10-11 12:02:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c067abdc-3e9f-3afe-bf7e-3c79290e96c5 | -17.36607 | -46.65802 | 2025-10-11 12:02:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d29c7d1d-f6e6-3c92-8b7a-a986f4df85da | -17.26509 | -46.89799 | 2025-10-11 12:02:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 42.4 |
| bf7d7e14-8ab6-3287-b61b-597ff0b7939d | -19.73208 | -43.89561 | 2025-10-11 12:02:00 | TERRA_M-T | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 412c7be5-442a-3b69-a040-90a07c30f8bc | -13.8686 | -45.8421 | 2025-10-11 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 280.1 |
| 83e9c54a-b00d-3f77-8761-c5d585a2f117 | -14.9825 | -45.5761 | 2025-10-11 12:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 110.7 |
| b69abd23-2e3d-35b9-9d52-7ede1b3e4a00 | -12.5093 | -47.4138 | 2025-10-11 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| f19f9a04-d1a2-3a2f-9dba-31c720858ac0 | -13.8496 | -45.8223 | 2025-10-11 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 440.3 |
| 8b42c42c-726a-3868-a0e5-5e051343c477 | -10.8341 | -47.1671 | 2025-10-11 12:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 215e940a-5369-35dc-bdf3-4fdf8ac4c292 | -14.983 | -45.5528 | 2025-10-11 12:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 109.2 |
| a6369eab-29b7-3d6e-a536-d1ed164c16c4 | -13.8491 | -45.8454 | 2025-10-11 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 192.6 |


[Clique aqui para ver as próximas entradas](README50.md)
