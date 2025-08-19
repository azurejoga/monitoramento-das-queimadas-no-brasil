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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc58cdf1-d343-374f-ad23-3cbc4c2cde74 | -11.34297 | -48.12921 | 2025-08-19 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0388b52d-0481-3d78-88dc-da2b7671c01c | -13.14183 | -57.16248 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a630efff-a845-3647-9752-fbee715028bc | -9.03652 | -50.17669 | 2025-08-19 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4498342a-b215-34ce-a5b1-ffae1a11bb8f | -11.81249 | -44.26153 | 2025-08-19 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0f37908-d6f8-3e69-9071-e2d4e67e65a7 | -9.26933 | -44.535 | 2025-08-19 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3733f1e9-a1ea-34f0-908a-32337c6b5ea4 | -12.6505 | -45.33153 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dfb6d45-15bf-31dc-ae6b-73eac9bf7bd2 | -12.62024 | -46.89296 | 2025-08-19 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cb04e9f-f572-36c3-9e31-237a9e6d9154 | -9.07185 | -60.4245 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cfdcb77e-823a-3772-adc8-ce57862b6de8 | -12.98488 | -56.85676 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3db5f853-398d-3f17-bd5d-76baf8e2b752 | -8.70561 | -50.68159 | 2025-08-19 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58e673f3-910a-32dc-8bff-f75b02eb08d5 | -8.82486 | -52.03682 | 2025-08-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1ba7ffe-6da7-3ad9-b310-55d60d74868e | -9.18954 | -59.62935 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5943ffc4-80cd-3261-9ca8-60266262c204 | -13.31208 | -50.79719 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfc2e61e-9694-395b-9bc7-ad874702e4c1 | -13.42823 | -45.90898 | 2025-08-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| beed86e4-ed62-3980-a841-3d3a5f6de268 | -9.19633 | -59.6258 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 38a69ba6-6c4b-317c-9c75-d859dfb501f6 | -13.3052 | -50.81689 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1635129d-c62f-3105-b07e-98dd0d1fa9f8 | -13.16596 | -54.9269 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67c5f85e-a5c8-397a-84fa-960ab7a7f9a4 | -13.16232 | -54.92137 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e4d27d7-e075-396f-b6e5-77e886b542be | -9.19524 | -59.63127 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4c7bfabb-7ed2-3c0d-b542-cdd8cebede5b | -13.25007 | -50.79898 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4619cbb-92d2-37f1-bbaf-b2ae660bd4ec | -13.01595 | -56.8341 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44c81c6c-596d-32f2-aa86-0ea39f1352ae | -13.43501 | -45.90576 | 2025-08-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12c837fd-b5f4-3570-9e33-03aa08b3ef31 | -13.18052 | -54.94912 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e8c6772-4c26-3b15-a3b6-580cacbd699a | -11.85805 | -44.88596 | 2025-08-19 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38bfd867-ce72-39c4-82bb-fd6776e77943 | -13.6145 | -46.89438 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09e155a4-0925-32eb-bb19-53c251131050 | -8.7708 | -50.02057 | 2025-08-19 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 94276e96-de87-3c59-bd0e-ca7b66dc6f0a | -13.13266 | -57.15368 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72e0af81-8cdb-30a0-9cce-c2d6c401aca4 | -7.25466 | -50.1731 | 2025-08-19 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1225f649-7bcc-38bd-87db-a131e2b7497c | -13.58945 | -46.99791 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 777bf282-ed30-3f9d-9463-168d9f353edb | -12.9988 | -56.84015 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f470acc4-ebc5-31bb-97b3-82b8c74af386 | -7.27076 | -50.16696 | 2025-08-19 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fbc52e60-c51a-38b5-a2d0-81bb6cdd992c | -13.17046 | -54.92775 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5af2025c-045d-31ab-be6f-d6dc3c8a76cd | -14.87104 | -48.05501 | 2025-08-19 04:27:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3de5e3ff-6e6f-3fd7-ac89-669e2e0b9e09 | -9.34108 | -48.51617 | 2025-08-19 04:27:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b88bb228-774d-3e34-87f2-cb867a641fc9 | -8.50266 | -44.75929 | 2025-08-19 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 132554f1-0d23-3bed-9319-c481af20dc90 | -12.99367 | -56.83911 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df60ebb4-1d9a-3e32-9778-b1fcd6ef9b96 | -13.31218 | -50.79689 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a94f1672-5d06-34fe-8e19-015ea9c461a7 | -8.70408 | -47.86374 | 2025-08-19 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| add5e6d3-a155-33f4-9935-c518d59f44ec | -14.85064 | -48.05533 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1353e9f3-adde-3827-97a6-cbef03180906 | -13.13725 | -57.15809 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6637c0e5-44d0-394a-a111-035cdb8c1a08 | -14.17175 | -45.30853 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fb0e2b2-394f-3892-aa50-8d5a4c176782 | -10.83272 | -45.04121 | 2025-08-19 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7fcdb224-8af1-37fa-b92a-04088347fa84 | -13.13914 | -57.14813 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30df0a1b-3bb7-31e4-8c0f-9be7849d6d03 | -13.18178 | -46.88222 | 2025-08-19 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7270981-1c02-336f-adca-1b22eb393efb | -12.96582 | -46.16893 | 2025-08-19 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 430d961d-104e-351a-a3ac-391309af28e8 | -13.44111 | -56.85555 | 2025-08-19 04:27:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c70647fc-89e3-3d1e-a14e-971a07400f29 | -12.98544 | -56.84312 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32292330-7a1e-34d5-8e9b-42b2f2e72917 | -12.99635 | -45.1883 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f54658ef-1a09-386b-8ced-b4b7c3a40238 | -9.18645 | -59.64138 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 28834dbd-cdaa-3abb-b9d4-e254b4d61d57 | -13.3108 | -50.805 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0a41f5f8-833b-3da8-8a16-52d68ec75457 | -13.14434 | -57.14931 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46a6309f-07d4-30e8-a6b3-3ac8bca494e3 | -13.44353 | -56.89742 | 2025-08-19 04:27:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db8e3cf3-fefd-36b0-b165-08b3e636463d | -13.56 | -47.01141 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13f0497c-30db-3a0c-a17c-4a375cb0f9a3 | -7.25751 | -50.15585 | 2025-08-19 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e9a9bb6e-44e9-358a-b499-818f470dcf77 | -8.70932 | -50.68221 | 2025-08-19 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| def0494a-456f-3071-932f-850cbc7d63c8 | -14.87435 | -48.05555 | 2025-08-19 04:27:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ebde594-43a7-347f-b533-1ad630e49c14 | -14.73895 | -46.30061 | 2025-08-19 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7aecbccd-b635-31e6-bbc4-e0765b94366f | -12.6496 | -45.82058 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc056d63-4732-3cd1-9ae4-4a5f94e19a3e | -12.73406 | -45.0521 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90c75b77-3bb1-3af5-85aa-17bb86cc4740 | -12.97456 | -56.84433 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc72f662-818d-3ff8-8284-2aa8fddffbab | -13.00452 | -56.83813 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1feb642f-f0f4-379c-a6bc-f8256733df88 | -12.30056 | -50.02081 | 2025-08-19 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2c9ab76-45d8-3247-938d-c8f2dc52f050 | -8.81725 | -52.05744 | 2025-08-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40230c87-702e-370c-95af-d0a76f81d556 | -12.91908 | -46.10467 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 303d03f8-8ff9-3b09-b66e-247c23bd0713 | -12.99388 | -56.86527 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29308f24-7212-346d-9604-a009caebbb27 | -9.81975 | -49.22443 | 2025-08-19 04:27:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1f0a7560-d2e2-31a1-94ab-7c4600438b00 | -10.3467 | -44.91028 | 2025-08-19 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6d2c29a-020b-3d4f-baaf-12b46968ef52 | -8.2376 | -47.86502 | 2025-08-19 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fbdca22d-f78a-3765-ba07-e5836625535b | -14.17357 | -45.31633 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9db70532-84af-36d9-9afc-ec909691077c | -12.98368 | -56.85245 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6614e6d0-76bf-32d7-94d8-88558792fb92 | -13.31149 | -50.80095 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 47baae73-1d07-386f-a687-9529f242f7bb | -12.97972 | -56.84525 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f5b778c-7816-3ba4-bdcd-ad45d4ab2115 | -14.16759 | -45.3121 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49c8721f-95ec-3065-bcb4-1465e46920d9 | -12.63847 | -46.9037 | 2025-08-19 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e30458f-fcc9-3e51-9fdd-c10f28fa9314 | -12.98875 | -56.86422 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e00f8b86-59d5-33f3-a613-db4218731301 | -9.18742 | -59.64037 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ba6315b4-b0a8-368f-b0dd-cbf936767ff5 | -13.13851 | -57.15144 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5723c3b-44cb-3dd5-b843-70526fbbd8c7 | -13.00391 | -56.84124 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e1437a9-5c30-30db-84f1-36cc2f71e7be | -10.96228 | -49.56564 | 2025-08-19 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a4ab085-4a05-3d2d-8289-fa709dc11309 | -14.50888 | -45.94144 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dfe0e18-21c9-3269-8d62-53bf7d3b95b8 | -12.63397 | -46.88832 | 2025-08-19 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9822b06d-3633-3a58-87a2-0d65684b89e5 | -13.19236 | -50.75253 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 969f5b18-8216-3e89-8ac2-f29b0fc5497f | -12.96473 | -46.17633 | 2025-08-19 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 855b4ce9-d83f-3cfb-8acb-8c432795a165 | -11.58411 | -44.85601 | 2025-08-19 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 615e90db-1eb9-313d-80fb-ae35eb1fd788 | -12.98308 | -56.85561 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 72c7f158-f353-34eb-a3d9-822f92961126 | -11.44901 | -47.32294 | 2025-08-19 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b332903e-606a-364d-9aee-1263ee738609 | -12.99873 | -45.19696 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a7c7867-1416-3eef-82b4-9c90c043d7e6 | -13.1578 | -54.92057 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc0974ec-8856-3bf0-8c1a-7716dce43ccf | -8.82829 | -52.041 | 2025-08-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c707882-66cc-3677-820d-0555a2a53c27 | -14.85119 | -48.05178 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0cd126b-64a2-36ba-af3b-532d1b67d9cb | -14.85174 | -48.04822 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7863e2d4-0a15-3916-b96b-4d8e38456f06 | -14.84844 | -48.06953 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aa23e267-d4d5-3ac6-8d43-c8e6a3bcbab3 | -13.00963 | -56.83923 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf5f12e9-9c92-353d-aaa3-5fde5b01bfc7 | -13.0033 | -56.84436 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20b2ff85-b81b-39c6-825c-7426d3f8884c | -12.29774 | -50.01637 | 2025-08-19 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddf8fd55-9f86-395c-b3ed-0c294de6d2d1 | -10.45902 | -48.80907 | 2025-08-19 04:27:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fdf42b26-a418-3f8b-afcb-3fd39541bcd2 | -12.99687 | -56.83899 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b81166ca-9267-3ed5-a6df-8ec67683f470 | -12.98486 | -56.84621 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83ff1c94-483d-30f9-908f-1363141956c7 | -12.51042 | -57.78038 | 2025-08-19 04:27:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 748cb106-7eb6-36b1-8986-b5ffc011e095 | -13.13203 | -57.15702 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README27.md)
