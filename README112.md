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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b744d23c-6ce0-31e2-acf7-b12613c46600 | -2.37017 | -48.58178 | 2024-11-09 05:20:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e26da013-477a-34c8-b505-b347e8cd8a2f | -3.35744 | -51.63951 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c276dee-2380-3718-b994-657a17cb7f82 | -3.0118 | -51.04535 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d543d29-0a38-39cb-9e73-9a0bf6d411f3 | -2.31088 | -50.67384 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bccba40f-f3e4-38a4-8e6e-ae26db30995a | -2.62528 | -57.03513 | 2024-11-09 05:20:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b726c324-e508-3d16-bf97-09ee8d7ae47d | -4.24284 | -47.5745 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a7c5b57b-2f62-3ed3-ae8d-cd9a5fe186e0 | -3.8139 | -49.85833 | 2024-11-09 05:20:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e0d4020-9fad-3dd0-a6cb-401bb69fc596 | -3.76424 | -51.7604 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d707493-83a7-38f7-b69b-d3d9c1d7f963 | -3.35226 | -50.12757 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1c652688-876c-30bb-bf6e-4d4a896bb7a3 | -3.01274 | -53.44159 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2c4f33c-c3cb-385b-a9f6-b8ab11e3cd97 | -2.71597 | -51.99471 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 74047af4-2497-3384-8ce1-49ab7aae97cd | -3.59244 | -47.34473 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| b2371579-c0e0-399a-a8ca-652ab5168e8f | -2.76661 | -54.05311 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 91e2de2c-136e-341c-8cd2-b3927a52b356 | -3.59507 | -47.34722 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 041687e3-c382-3031-bdac-2e8290e60a78 | -1.25614 | -55.7105 | 2024-11-09 05:20:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bf95834-74c8-35bc-a85d-91ffc2775af5 | 0.62244 | -60.0942 | 2024-11-09 05:20:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ccd6773-cccc-3b7b-b950-8d5ba99eb058 | -4.30489 | -50.74319 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1acb8013-8883-3145-9d69-bff8149249dc | -2.23214 | -48.37119 | 2024-11-09 05:20:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dda61966-565a-3e82-8c77-8e7aa48e3940 | -2.3634 | -54.75129 | 2024-11-09 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1f0d1c7b-ca1b-39b3-aaea-79e139332c5f | -3.2364 | -50.44765 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c4350df-3ab1-3283-b2c7-ad9235a313ab | -1.55695 | -52.27042 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d39018cc-0871-33b2-be1e-254c37961642 | -3.14941 | -51.12548 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a95f613-0e99-386f-987b-4bf779b28f90 | -3.15574 | -54.47604 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d06a1aa-3b28-36d6-ae23-a5ab74a15e7f | -3.03264 | -53.27441 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a5a89b0-0372-366e-9c6a-ee9fa85e7fcf | -2.23158 | -46.54789 | 2024-11-09 05:20:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0b1bc47-c387-36a9-b742-190a0fba558a | -3.2408 | -50.45527 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3ac39a1-d5fc-3a27-b232-235a4b28b042 | -2.61979 | -51.29888 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 58caf1eb-f76e-34a0-9e9e-ad5783155124 | -3.76792 | -51.38198 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c281891f-64e8-37b4-9842-1f73e4a63d03 | -2.92236 | -54.19733 | 2024-11-09 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6d7ba93-f760-3f75-a788-9cfa55e598c4 | -2.41354 | -48.84551 | 2024-11-09 05:20:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae594012-9104-3976-bff7-3a2a7f6f3322 | -3.06822 | -54.7766 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7770c181-bdd2-3895-b4cb-9cbb7e78ae64 | -3.02025 | -51.19902 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d061a38-ce94-39b5-befe-160896141a74 | -3.14694 | -52.97128 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3745ea64-9b87-3635-af89-08d186a9edc8 | -3.15458 | -54.48355 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c5ea0fe2-5635-301f-9d4a-9a1056ef89ec | -2.44808 | -46.32372 | 2024-11-09 05:20:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0863ee2f-347f-36af-8d63-8bc02c276c48 | -2.91834 | -49.36746 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a48c525f-1218-3a75-8252-64b0d2a2683b | -3.04534 | -50.36683 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78b0e015-4e4c-3110-ad87-23ca5d3663ed | -3.75104 | -52.09949 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23ba1582-883f-3489-8476-51605d8230bc | -2.94255 | -52.70879 | 2024-11-09 05:20:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69435a10-1251-3044-af21-7ad77d56f728 | -2.16201 | -53.65052 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2a8d702-57cc-3e80-8b49-655f6dbba2fe | -1.16867 | -54.16007 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 103b048a-cdcf-3851-af84-719c8a7c2299 | -3.3258 | -49.91675 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fd5c6fd-613e-3cdb-bac3-be32dd91a879 | -3.69565 | -54.61934 | 2024-11-09 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5dfb3a3c-4ab0-3a9d-95a0-6a4de5ff822f | -1.2473 | -53.38594 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48a44260-0a3e-3cd3-aa1c-a7af7f8073f7 | -3.97188 | -48.1677 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a055476-f23a-3b02-b4b9-1f6d9e8a80a1 | -3.88752 | -50.24108 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4073da01-8e60-37ee-b72d-48849bc700c2 | -2.8758 | -51.46833 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09db6e6e-53da-30ae-b251-b9b18cc329c8 | -3.18517 | -54.31227 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a68ec34b-cac4-3d6a-b0ff-df46c5f74dba | -2.57952 | -49.13625 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8432e76f-148f-3c63-8d65-bdf81855397d | -3.20291 | -50.63238 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 921937c9-eca9-36f5-9a19-7573b7d39cad | -4.09085 | -48.85579 | 2024-11-09 05:20:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ecebf92-6c4b-3b35-bf09-250c5770594a | -2.84931 | -51.77609 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 211fc416-5196-3473-b4c2-9709ed814503 | -3.08407 | -50.56432 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b99a5d16-a429-30aa-99e8-98c1f3be0d35 | -1.22106 | -52.1324 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34fbc476-12d9-31cc-a384-6faea8e5e378 | -2.18594 | -53.63761 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c9fe5e4-4a9d-3f90-b8c5-631b323565bc | -3.07869 | -50.56354 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a9359ab1-f68e-3afe-99ee-9065b3301c9a | -3.24836 | -50.45349 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e6f773b-924a-3b58-91f9-9b97108781a6 | -2.94168 | -54.12571 | 2024-11-09 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b890b33-b314-3398-9ff7-f6fb53832b17 | -2.60321 | -51.30553 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c899a92-b4b2-39c2-b562-bd156367a713 | -2.87906 | -51.31586 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| caf8cc24-7c36-31e5-a832-1a4abc0f6b6f | -2.34026 | -50.51638 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3726b84d-745a-39a9-8831-05e4fe0b21c1 | -2.80998 | -52.99732 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a7db9bb-3f8f-3dd1-92e0-f7ff7f848f24 | -3.32253 | -49.91613 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6c97742f-2f0a-30f8-87af-dce7a7b82c74 | -0.39149 | -51.94804 | 2024-11-09 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78d8b25e-1e45-3b48-80f6-231e25b3871f | -3.89729 | -51.92848 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b703a3ff-a799-369a-b978-7ce1239ffcfc | -2.98491 | -51.46378 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70f5b5e7-cc4b-355a-a5bc-b86584d878b8 | -2.20479 | -50.34011 | 2024-11-09 05:20:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02625fe9-7c3b-395f-a74c-6fc6b9cbfc4c | -3.03808 | -50.30442 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a7792f8-8a66-353a-9c80-b542214df16a | -3.48877 | -54.57809 | 2024-11-09 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b594c200-6225-3617-851b-71037a840a26 | -3.02072 | -51.19593 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24d3aaf8-d513-3d1b-aefd-e6ce05158f2e | -3.23796 | -50.44851 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc3e9d48-e980-3e44-9c88-10e8c8579c10 | -3.38594 | -52.35873 | 2024-11-09 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4f04caab-13a9-3ec5-890f-9bdc99e311a7 | -3.58916 | -50.2412 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dd67621-6723-3a2c-ae4d-1e33f98564f9 | -3.72527 | -53.39863 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3cadeb0-8ca7-33b6-9538-e5dd0c2958ef | -4.38652 | -48.58084 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2fc0686a-c3f0-3e39-8792-0b2ca81f22a1 | -2.92179 | -51.67588 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f761cae3-c8eb-31fb-8db6-ffac7ef0f8d8 | 0.84652 | -50.17391 | 2024-11-09 05:20:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61c6bcb8-8154-3f74-9f33-21e5a474971d | -2.94328 | -52.70387 | 2024-11-09 05:20:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0357bec5-9657-33c0-a755-fe047d33eaf1 | -4.20583 | -53.73207 | 2024-11-09 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ae3a04c-f287-3c19-95d2-f1af43d9509f | -2.58609 | -51.9227 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60fee810-9ecd-3b2d-ba08-8c61fbb06ccf | -2.96301 | -53.86703 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d391c1f4-3836-3bfb-b240-4788327e8c9f | -1.21637 | -52.1317 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4a4704c-77e2-3bc7-a6f9-1ad4abc4a096 | -1.19306 | -52.15844 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ea42e2cb-36dd-32b3-a19f-929a02d536c5 | -1.39068 | -51.57088 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd056a7b-cf31-308d-9758-e9b3b5bab6a9 | -2.60962 | -51.7499 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6becacd4-8e00-3cb9-8e29-2179099e40f9 | -3.76381 | -51.76329 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2bbae67-d13c-3fb9-99e2-c89cc044f58c | -2.45024 | -46.31772 | 2024-11-09 05:20:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 130b20e9-8ceb-3b4f-867f-8d2547ab6e16 | -3.34505 | -49.94286 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0f25428-23ad-342e-9d81-84a570e70e14 | -3.2434 | -50.44933 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 125408d7-61e9-3db1-a23b-b6b45552fd94 | -1.56154 | -52.28811 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 63edd086-2ce2-354e-babf-a6e1c40d02c9 | -4.62173 | -46.53916 | 2024-11-09 05:20:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9422145a-b446-38b0-9adc-0908971b4f22 | -4.38986 | -50.97209 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3e39ff8-2d15-3d0e-b0ed-e3290532d32c | -2.8146 | -51.80492 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 700d848d-0edb-3db8-a583-f2c3ae4e8f44 | -2.6724 | -49.89043 | 2024-11-09 05:20:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04690edd-ba7b-3439-b319-360e3e8016ae | -3.28254 | -51.52498 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cfed78d-dd9e-3bd6-8b64-ed24e095f7ca | -2.71517 | -52.00006 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 610ac340-8b6a-32eb-851c-5b428143ac63 | -3.22964 | -50.26931 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc5a9b15-f8ff-3411-b66c-6940fa28787b | 1.08634 | -51.30584 | 2024-11-09 05:20:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2681229-3333-3d05-b2ba-024b8d8c3b86 | -2.91618 | -51.67928 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6621b83a-161f-3fbb-8167-dcf54d2021b6 | -2.24991 | -53.66687 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README113.md)
