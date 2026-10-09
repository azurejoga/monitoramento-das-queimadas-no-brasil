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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18b92175-399d-3141-8166-45d7dcec5015 | -2.7559 | -54.11294 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df75669d-d36d-30ea-8d30-fb75e6ed577b | -2.8673 | -40.01456 | 2026-10-09 05:01:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9947ae28-e566-3db7-b938-ea8ad985deb7 | -3.35143 | -50.40813 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fe91bd3f-cc80-39cc-a06c-b7e7d03fb9ac | -2.18966 | -48.24795 | 2026-10-09 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f7135cc-422b-3224-83a1-1cb27eb6aea5 | 2.77007 | -60.01033 | 2026-10-09 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d847a74e-f2d8-3278-b747-3ad74b780797 | -2.74188 | -54.11068 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7293415-d134-399a-ad70-68fb5ab40073 | -1.63949 | -55.27808 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2985e93-0273-3da1-b3bb-81c76bf35dc7 | -1.15333 | -54.22851 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4583d254-dd2d-3776-a79b-31a3e0c06de6 | -2.99117 | -48.91344 | 2026-10-09 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c222d1a2-9872-3d12-84f1-5f5ad89ffdfd | -3.17175 | -50.59661 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dedd10f-20e5-3c4b-9f26-0cba387293a4 | -3.50147 | -49.94049 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25c659ea-22ba-362c-8500-f2aaaabb43b6 | 0.55188 | -51.66146 | 2026-10-09 05:01:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 380b32f4-6213-3da3-b5a4-9d9d8541bf9b | -1.73747 | -52.24257 | 2026-10-09 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ed859a63-0a12-3add-ba49-5e0ede2e271e | 3.73612 | -51.61561 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c6008cb-6b4a-3cbd-9e8b-a8de1b4af4c9 | -3.27639 | -51.06712 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c644dc79-1650-37fb-9257-ad8745bd5294 | -1.49216 | -54.55283 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c403eda-8094-3bbb-b902-0a68eb9cf273 | 0.19257 | -51.35566 | 2026-10-09 05:01:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25c71da0-1053-35cd-8408-52362274faa9 | -2.37562 | -48.2252 | 2026-10-09 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd778fc9-19d8-3c27-9c2f-758647feefa1 | -3.36318 | -50.48722 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11e2827b-68ac-3200-a343-5e715269b955 | -2.51507 | -56.268 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 574d5a11-7a61-37ee-a83c-8894792de897 | -3.16613 | -50.58845 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c17c511c-cd1b-3331-b634-7a9615a042dd | 1.6992 | -55.59994 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e60b2892-53e4-3cb5-8a2b-4c97173d6922 | 3.55323 | -51.276 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dba15276-48b8-3533-b39b-0ece17c2c51b | -3.19533 | -50.55653 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52d1080c-8e74-37c0-9f3f-01b232caf59b | -2.75837 | -54.09744 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c75f361-7c08-3a04-a092-728d9d995400 | 0.53875 | -50.89447 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af9190d4-5410-3b08-8cc4-f4126497705c | -2.46009 | -56.08926 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f2943bc-b036-304a-8dd0-d9eae340965f | -3.35763 | -50.41279 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef617e65-fb33-3995-8768-9a9ddef79942 | -1.405 | -55.41428 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab2a449a-92a9-3877-b248-bbec7e771844 | -2.73526 | -54.12952 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe36785e-fbc3-3b49-aa35-dabadcb5912b | -3.38571 | -50.21324 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6732a0b5-19d6-3800-adfe-4376faac3bdc | -3.35022 | -50.48152 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4ffed1d-258f-3d8f-b398-2f2809074f53 | -2.39424 | -51.29963 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f634e0e-fd50-363c-b8f7-ca414cfec34e | 0.44011 | -60.53143 | 2026-10-09 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0558db4-d103-3776-9651-dfeeed00b2f0 | -1.10959 | -54.16898 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f68f96f3-04d4-3d6a-9a1c-9b7ff2e9933d | 1.16164 | -52.73421 | 2026-10-09 05:01:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d3ec41a-5038-32bc-a964-80eb2a9a3341 | -1.60794 | -55.16006 | 2026-10-09 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 949e6a14-e635-3a53-bf2d-c3621c7ed469 | -2.49726 | -56.17802 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6a419d07-43c6-383c-acd9-8cce0cace48b | -2.84608 | -54.13422 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c15e7ecb-5a31-3bbd-a0ef-c900f15a1bd5 | -3.19926 | -50.55349 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44dbd2f9-dc00-3fd9-8718-502c52df7bde | -3.17398 | -50.58239 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c338fb21-1744-3b7b-bbf1-821f52640df9 | -3.34633 | -50.41841 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a9dba754-9974-3ca7-8225-f941f2e0a885 | 2.32619 | -50.87542 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90345ef9-7023-38c5-96c7-597711f511f2 | -3.17231 | -50.59306 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 449710b5-e397-3dd9-8090-e04177271369 | -0.99481 | -47.65404 | 2026-10-09 05:01:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6de9b7a5-616c-33a9-b5fc-be5d9c222930 | -1.14748 | -54.21925 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01f020c5-9e5f-358e-9404-ab14824f91b5 | -4.15155 | -43.18874 | 2026-10-09 05:01:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a56a8cb-8207-3cf6-b1c5-a60db45868e2 | -2.50674 | -56.1693 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3094a76e-8932-3fd0-99c7-85d3e8b783b7 | -2.49575 | -56.1625 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5030ae66-af86-3ef7-8802-e10130822706 | -2.5084 | -56.13424 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 939b3e48-7b17-35a5-9893-8556a72412ee | -2.75941 | -54.1135 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edbe47f6-3b9e-3d67-b828-39bd01e50e96 | -2.74125 | -54.11456 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f14f7d6-a54e-37f3-98fb-9c771f9693e8 | -2.46475 | -56.05992 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79f72172-499f-3aae-a5cb-41003afb3aee | -3.50205 | -49.93677 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44936e00-7d12-3d8a-9912-2b8d554a7a59 | -1.32466 | -52.44815 | 2026-10-09 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4923b94-4e43-3793-a46e-a6c67173790a | 1.68873 | -55.61226 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9725bae-04f7-3072-afbc-f4b99fb45c5d | -1.61431 | -55.12011 | 2026-10-09 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53bb9a29-9a59-3561-849b-d9349a7df903 | -3.15827 | -50.59451 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ae7f0b4-b19c-3188-927f-59c1bb1aa487 | -1.28392 | -55.42058 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a5f2cf2-4384-319b-b148-7f21f37a9434 | -3.00808 | -51.01501 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4348303-e3a1-38d8-aa80-cebf70b76fa4 | -0.99527 | -47.6572 | 2026-10-09 05:01:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c212757-7345-3af9-a5fc-920034fffd37 | 0.53211 | -50.89552 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e395fd56-1f12-3dfd-9d77-58dabbdf2303 | -1.05427 | -53.59063 | 2026-10-09 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08c9461e-bd88-3a26-9489-f63c74ceff9b | -2.48522 | -45.66965 | 2026-10-09 05:01:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c1d4a01-f534-3a86-bab6-9fb65c87bcf7 | -1.21049 | -55.64819 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf4331bc-c8eb-3d70-a2d7-79dee620197c | -1.20824 | -55.68747 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| caadf8ed-759e-3938-9395-5aadf96d7e52 | -3.27249 | -51.07009 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1ac9848-89ff-3575-bed2-80deb7b200c5 | -4.0874 | -44.12051 | 2026-10-09 05:01:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e89ba341-e9e8-3910-8263-681f2aa0aa38 | -1.5934 | -47.35441 | 2026-10-09 05:01:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ea31e30-d83b-3b2b-b60d-2435efcc03f1 | -1.05366 | -53.59444 | 2026-10-09 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 15c0c3cd-6b3e-3727-9f2c-0e46af5d906c | -2.83431 | -54.1403 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d65b2798-3d70-35e9-8572-4a2e340e73ee | -2.83845 | -54.13696 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cfb612b4-2bbc-3caa-b255-6d8faad58d0e | -3.35482 | -50.40866 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f146d88f-16d8-3e87-a13f-dd3147830ffa | -3.17791 | -50.57936 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f57686c9-2722-370f-8f17-3e31b490c8e6 | -2.74765 | -54.11956 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 32a8ecea-1e81-34be-a69c-c0bdec9cb599 | -1.48986 | -54.54388 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d28798e4-aa17-3050-8cc3-240625fbb36c | -3.30438 | -49.12697 | 2026-10-09 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6651a654-c06c-38b8-9a98-652108ea7b25 | -2.51983 | -56.26363 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3dd808d-efc0-374e-8e6e-fb5232ba3c28 | -2.21749 | -55.45271 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 82636933-c350-3913-802b-3a77bd72d4ec | -2.78587 | -51.66875 | 2026-10-09 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96a864a6-9e9d-3a6d-a25c-06fbb5323e87 | -1.74081 | -52.24309 | 2026-10-09 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd67c83c-9387-38b3-b6d3-823d7fb817e1 | -3.19814 | -50.56062 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 595b013b-8827-3b21-a116-7f66740d1a0c | -0.04738 | -50.82772 | 2026-10-09 05:01:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a41a4abb-f662-34d6-941e-f1e8128dacc4 | -3.1841 | -50.58396 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e2e4230f-eae2-3131-b82a-8ba480fea61c | 0.44068 | -60.53506 | 2026-10-09 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84654457-fce1-3e51-b698-21073c68b243 | -3.30281 | -50.23011 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5c7f2824-deec-368f-a7c2-aa288981cd2d | -3.36602 | -50.47256 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0673453e-c1f0-3093-b340-371370216b35 | 2.42169 | -50.8175 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8ef4a973-50cd-3804-b2a9-9183a70967b5 | -2.75652 | -54.10907 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25678780-64f2-3232-ac1a-c647c1158915 | -1.83168 | -54.99397 | 2026-10-09 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35ac26e9-b1df-3e87-bcce-1b9830f455ad | -2.16338 | -54.45857 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0404a84a-82c1-3c2b-8b3c-728ba89fe07a | -2.02676 | -55.62806 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f270759f-bdeb-3f36-9097-f09aba925c70 | -3.17051 | -50.45017 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb6408dc-18fb-3e7f-b817-a9ba9fd62696 | -2.46397 | -56.06482 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ae1c94e-5258-3a6a-b379-34707bf445c0 | 3.55267 | -51.27247 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b9ed61a-b433-39af-a3d4-a9152ce55cad | -2.50315 | -56.06789 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0037845d-d8e6-370a-a08f-a188ba76e777 | -1.53995 | -52.75847 | 2026-10-09 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29caf8d3-0dd6-325c-9a81-db60a5ca4d94 | -2.22382 | -53.6986 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6524fb4a-2123-353d-b775-72e4a98d76a5 | -2.74245 | -48.42766 | 2026-10-09 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 439b92a2-c352-3265-8245-d441b0badf11 | -3.35029 | -50.41534 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README129.md)
