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

## Dados Diários - Página 260

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b3fbfa5-5887-333d-94bc-45272db0377b | -6.1615 | -52.6676 | 2026-10-07 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d425da9c-9dec-3d27-8104-98b7be2156c6 | -5.9772 | -43.5057 | 2026-10-07 19:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 6b55f7bc-0481-3701-a1ac-56ccf246b0d7 | -10.9938 | -45.4985 | 2026-10-07 19:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 60de5a13-a049-3c30-b7b4-c804810cfc2b | -3.2451 | -57.8693 | 2026-10-07 19:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 6d5027a6-2dcc-3380-83c0-48454d395ea2 | -3.5862 | -54.6541 | 2026-10-07 19:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 322.8 |
| 1c6c789f-1592-3c0e-bbd0-ca1f34c50cee | -9.0592 | -65.9209 | 2026-10-07 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 093cf4aa-c70a-3c02-8db5-d6b1877a3db8 | 1.6937 | -55.6461 | 2026-10-07 19:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 41f391b8-2b27-3f1b-8220-39d34cc5314f | -13.9866 | -43.9284 | 2026-10-07 19:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 73356161-0984-3205-9e50-77c8a32e95ee | -7.2011 | -52.6272 | 2026-10-07 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 69b631c0-f208-3d2d-96d4-b5ae3a22a5a5 | -6.8764 | -43.685 | 2026-10-07 19:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 2c78f904-c9cc-30cc-ad0a-f18afb97ccc0 | -2.9327 | -58.3204 | 2026-10-07 19:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 61a84d97-2f81-3af7-b9fe-46f5b300976e | -12.1922 | -44.7953 | 2026-10-07 19:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1020.2 |
| f46f7d34-4944-396b-9c9e-91646f21650f | -8.5366 | -67.069 | 2026-10-07 19:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 154.2 |
| 9ce149a0-66c1-32c7-bf74-bd4660f4794b | -6.0447 | -53.49 | 2026-10-07 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ea132b34-2dd5-385e-a26f-9ffa2352dd68 | -4.777 | -55.7104 | 2026-10-07 19:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 41050965-e3fa-33da-9393-864b72ac632c | -6.1298 | -51.9281 | 2026-10-07 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 136.1 |
| ce8c0a75-7d23-31fc-a331-0fbc3a2e17dd | -6.1429 | -47.9432 | 2026-10-07 19:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 1d420605-93e8-3fa1-8ed9-561b80a6f45a | -9.4751 | -64.3336 | 2026-10-07 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 352c2855-f1d7-3bf1-8c8a-d7f665e99b68 | -6.895 | -43.7066 | 2026-10-07 19:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 128.0 |
| e2bda4da-0bbd-3470-9c62-a5eafaa47a9a | -9.5468 | -64.8196 | 2026-10-07 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 106.1 |
| cb849f87-8846-3486-9fb7-f4f6ad266f70 | -5.8966 | -53.4975 | 2026-10-07 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| dd3fa14c-d365-3b02-b5c8-db6db36617c1 | -7.3935 | -46.2144 | 2026-10-07 19:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 54ef8ef8-da24-3730-ab2d-27791d9a5934 | -8.5551 | -67.0686 | 2026-10-07 19:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 896562a8-3e65-3bd9-ad3c-1d516d1761c3 | 1.7121 | -55.6063 | 2026-10-07 19:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 94047040-f582-3c9a-bcce-253ff8e33a81 | -6.3165 | -43.3381 | 2026-10-07 19:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 2df9b773-d88c-3ced-ae78-406a58c5822b | -4.7769 | -55.7302 | 2026-10-07 19:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 7f6b20e8-cb27-3330-8b65-ba35a6e2de99 | -3.6786 | -54.5115 | 2026-10-07 19:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 09fb1d85-f944-31e1-8db1-e5dd36049bc4 | -7.6767 | -72.3142 | 2026-10-07 19:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 192.6 |
| 0c65a26b-3fad-30cd-a0c2-fa62d82b237e | -5.7305 | -53.4446 | 2026-10-07 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| c43f312c-0631-3223-b2f8-2441f8a0c793 | -3.8036 | -47.5057 | 2026-10-07 19:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 8f52ad71-1448-3030-8371-4a39c7fce656 | -3.3134 | -53.8592 | 2026-10-07 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 5cff1665-a28e-3518-b147-c07d30eb4a9c | -6.1617 | -52.6471 | 2026-10-07 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| d31592e8-2184-3af0-b2a2-6d6298f1cbff | -6.8292 | -39.5472 | 2026-10-07 19:30:00 | GOES-19 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 97.4 |
| 8a9ebf14-0ff4-3dd0-9ffb-709fb8e86ab6 | -9.0407 | -65.9215 | 2026-10-07 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 159.9 |
| 0a3520ef-306f-341b-a705-69586bb6ded5 | -3.4763 | -50.0673 | 2026-10-07 19:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 2b74fd88-5116-34a6-8bda-d582c46a741b | -5.6932 | -53.487 | 2026-10-07 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 377.4 |
| ca80fc53-32cb-32b3-bc4c-c09ee9c1a4d5 | -3.328 | -50.1775 | 2026-10-07 19:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 187.0 |
| 8a1d5f69-67f1-3070-bde4-0a5550796a14 | -5.8205 | -53.8255 | 2026-10-07 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 3e2da7fc-faf4-3747-91c1-015fe2b7ca1a | -5.9699 | -46.3714 | 2026-10-07 19:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| ff20f741-c7f7-32b0-8b11-432e94800031 | -2.6859 | -49.0325 | 2026-10-07 19:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 376949c0-e210-34a7-9d5e-ba372e164ffa | -9.5004 | -66.7831 | 2026-10-07 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 1e24e132-e399-33ba-ad1e-38c8eb512209 | -5.9043 | -43.2784 | 2026-10-07 19:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 213640cd-1841-3ca9-86a8-c072ae672f2a | -9.8821 | -44.8402 | 2026-10-07 19:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 1d04866a-fdfd-314a-89af-6c64944691ee | -11.6369 | -43.6876 | 2026-10-07 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| a4e0ce15-4702-393e-bff2-7fa2bd2d5d3a | -3.5865 | -54.5742 | 2026-10-07 19:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| cf802527-4ee5-3c94-b574-e92c8bedb0f3 | -6.6039 | -53.0116 | 2026-10-07 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| a025cf63-8a9a-3771-9b75-bd0f3d37c6f5 | -4.3044 | -50.7909 | 2026-10-07 19:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 41852d76-2d57-3197-8822-500481726441 | -5.9649 | -40.914 | 2026-10-07 19:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| cd3f1e15-2155-338a-8c74-b82c5952cb8a | -7.1827 | -52.6078 | 2026-10-07 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| bfabc47d-4efb-3686-969f-e83c5fbbde4b | -5.7304 | -53.465 | 2026-10-07 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 4604683c-fe99-3acf-913a-2aa4317f153d | -3.5684 | -54.4946 | 2026-10-07 19:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| ab99a5fc-e5ea-39cb-b66d-2d829309aa22 | -9.4509 | -45.8271 | 2026-10-07 19:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 25b6f998-3957-3a79-8874-1725a17d1800 | -5.051 | -49.7677 | 2026-10-07 19:30:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| b1a21522-9784-3a31-aebb-7518f2fc2b74 | -5.9644 | -40.9627 | 2026-10-07 19:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 141.2 |
| e96a6770-5faf-3e55-af50-46cebc8374e0 | -3.0069 | -57.9129 | 2026-10-07 19:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| cca6ebed-c36e-3284-89bf-ec31372e84b7 | -12.1926 | -44.772 | 2026-10-07 19:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 1ba48d6f-6152-3fbf-910f-10addd4b1626 | -4.2744 | -46.3846 | 2026-10-07 19:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 163.0 |
| b01e11dd-fe05-3e11-9f0c-cc5dba31ac65 | -3.1697 | -58.6244 | 2026-10-07 19:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| fc90a5ce-c03a-3a2a-b2df-75aefbb54df2 | -5.4771 | -42.8427 | 2026-10-07 19:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 117.9 |
| 25bc71a3-8bd6-3099-92b7-827049b4cdd3 | 1.7488 | -55.5861 | 2026-10-07 19:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 098f26d2-d4a0-3592-9bab-81017eab4562 | -13.3865 | -43.8708 | 2026-10-07 19:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| e7858e59-25bd-318d-aa88-838504da6db3 | -1.1094 | -54.1601 | 2026-10-07 19:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| c04fb2f6-5ab1-3e1d-8218-4cd8b2b888da | -4.1223 | -54.0158 | 2026-10-07 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 8513a8fa-a1a3-3bb6-9c6b-86cdec9d7518 | -5.2274 | -48.4113 | 2026-10-07 19:30:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 51.0 |
| bcd1ee98-d1b5-31bd-8cfc-001fa9a49f49 | -5.9647 | -40.9383 | 2026-10-07 19:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 217.4 |
| 4db774ff-0195-31f8-bbf6-cc488315af5d | -9.4506 | -45.8498 | 2026-10-07 19:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| d9f8136f-9203-3326-ae09-6dccc6defcf2 | -3.6603 | -54.512 | 2026-10-07 19:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| a16d98e3-23ff-36ad-a047-d10e4f86af29 | -6.3351 | -43.3598 | 2026-10-07 19:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 43e29679-ff2f-3c0a-8370-52601e23a8d4 | -8.5184 | -66.9954 | 2026-10-07 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 96787543-3609-3dff-956a-6883e82eacc2 | -3.3452 | -50.4707 | 2026-10-07 19:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 218.7 |
| 0b6cbb87-cc17-30ea-8a41-696de5813087 | -5.749 | -53.4437 | 2026-10-07 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| fbb7dbdb-68aa-3adb-a9ba-3ceac721488d | -5.9835 | -40.9367 | 2026-10-07 19:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 116.4 |
| fc78cc6b-1b3e-336e-bafb-5fd8f834bc50 | -6.1431 | -47.9214 | 2026-10-07 19:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| acfb1a3f-2f09-3d4f-945f-c5b1402f6fa7 | -13.3676 | -43.8504 | 2026-10-07 19:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| a50510a1-18c9-36c5-bcb1-308365abedd0 | -3.2957 | -49.1202 | 2026-10-07 19:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 0fb2b847-e0b8-3a29-aad6-ffd1eadc8908 | -7.4697 | -42.8315 | 2026-10-07 19:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 553dbce3-dc41-3322-9526-d8218c35e6bb | -9.1362 | -65.3022 | 2026-10-07 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 556679b2-aafa-310c-8e81-5e3ee1a0cc7e | -8.9769 | -45.9475 | 2026-10-07 19:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 212a95dd-114f-30cf-97bf-0f0b37d0d0dd | -9.0591 | -65.9396 | 2026-10-07 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 136.5 |
| da231ade-5e2d-37f8-aff5-51f5a93d02b8 | -6.0075 | -53.5122 | 2026-10-07 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 52312c4a-c649-3fbd-9281-e1bbb1a60bf6 | -3.2199 | -54.3038 | 2026-10-07 19:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 925b9223-5e06-3c1e-93f2-44b0adf1f119 | -6.9331 | -43.6566 | 2026-10-07 19:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 46d8008e-c530-374b-8381-4be96f8c8722 | -6.6224 | -53.0105 | 2026-10-07 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| e426ac4a-09e3-3ce6-b085-75a8c8427e5a | -3.7818 | -41.6479 | 2026-10-07 19:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| af7f3875-e01c-322c-bcd2-4d053808878f | -6.02 | -51.7272 | 2026-10-07 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 6c7a5cc8-92ee-3b8f-8378-ad107b49470a | -5.9512 | -46.3727 | 2026-10-07 19:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f14ac4fe-7cc7-37bb-be8e-87a1a156932b | -6.9937 | -40.0277 | 2026-10-07 19:30:00 | GOES-19 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 878ac35b-80a3-39a4-923b-b9c7c3beb9f2 | -13.3671 | -43.8742 | 2026-10-07 19:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 384.8 |
| b2233b5f-f833-3fbb-9297-e20d1d8ffa60 | -6.1484 | -51.927 | 2026-10-07 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 182.2 |
| 0a5c0102-936c-369a-8673-d370e189c393 | -3.7166 | -54.2297 | 2026-10-07 19:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 35a52687-8620-326d-baba-387806068528 | -3.3133 | -53.8793 | 2026-10-07 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| a3b8bee8-a15a-3850-881a-acb0e9ada862 | -4.1574 | -44.2726 | 2026-10-07 19:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| f369db2c-842a-3306-8525-c694c7600c08 | -6.1402 | -53.0574 | 2026-10-07 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 9fcdebc0-71ad-3c76-855a-44d512a06937 | -3.5875 | -54.3138 | 2026-10-07 19:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 1fc14869-58c7-3891-a50f-2f50099f4947 | -5.6934 | -53.4667 | 2026-10-07 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 166.5 |
| c50c4cdf-3010-33c5-9dea-45851420c101 | -8.6036 | -45.6482 | 2026-10-07 19:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 265324ae-67bd-343e-9d8b-11d672ef0571 | -3.2267 | -57.889 | 2026-10-07 19:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 86675c0e-f5c3-3970-a8b6-148affd79b52 | -8.6106 | -67.0486 | 2026-10-07 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 177.8 |
| 6fffe2c1-2498-39ec-8cf3-a084dc4a1ee8 | -6.9747 | -40.0297 | 2026-10-07 19:30:00 | GOES-19 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 5e7c4e2e-4231-337a-9045-5f04c9582caa | 1.7121 | -55.6261 | 2026-10-07 19:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |


[Clique aqui para ver as próximas entradas](README261.md)
