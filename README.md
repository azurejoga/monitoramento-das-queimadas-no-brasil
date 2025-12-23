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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0884a72-e82e-34b5-adb9-80a5881310c6 | -21.5022 | -48.6492 | 2025-12-23 00:00:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 5ce41f3b-e74e-3463-b4cd-b7c0f43450b6 | 3.511 | -60.8906 | 2025-12-23 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| eba5a3c3-4d66-3ccc-95fd-094deca2ef0f | 3.4927 | -60.8909 | 2025-12-23 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 46.9 |
| ee07a0a5-0423-3626-9617-36f98526554e | 3.511 | -60.8716 | 2025-12-23 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 30.8 |
| b6a1bb85-a84f-3c7d-9aeb-5b0d8dd73e67 | 3.4927 | -60.8909 | 2025-12-23 00:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 2e1e849b-13dd-3473-86a5-6d35e21803f8 | -21.5022 | -48.6492 | 2025-12-23 00:10:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 52a4bf43-8476-3859-a5d4-2456c4321ff2 | 3.511 | -60.8906 | 2025-12-23 00:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 262f3598-4c61-3925-8bdd-8e011a28085d | -21.5022 | -48.6492 | 2025-12-23 00:20:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 96.1 |
| eb631e75-87b8-3778-a8ed-747b3d6587ae | 3.511 | -60.8906 | 2025-12-23 00:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 50.1 |
| cf5e7ab2-5ce0-3fd7-a2e4-0f76d53a8f5d | -21.5022 | -48.6492 | 2025-12-23 00:30:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 3384d850-e6ef-33bd-bff7-f8bd5a8e086e | -17.7805 | -42.108501 | 2025-12-23 00:31:00 | METOP-C | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a94e6837-9ee1-3692-8e11-a463afb4b315 | -21.5007 | -48.6483 | 2025-12-23 00:31:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d1360671-47bc-304d-a8e0-31ddf20b0609 | -21.0445 | -49.594799 | 2025-12-23 00:31:00 | METOP-C | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 51ec5af1-b20c-3924-b9f0-45cb4c90517c | -1.4933 | -45.911201 | 2025-12-23 00:31:00 | METOP-C | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ba1eb361-9271-3617-a6ea-301488fb7285 | -21.498301 | -48.6353 | 2025-12-23 00:31:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fc9e6e7e-bd23-3cf0-877c-c90bb37972eb | -21.041901 | -49.5802 | 2025-12-23 00:31:00 | METOP-C | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3cb11884-e17e-316a-8e22-886ee9501ab8 | -21.374201 | -48.6203 | 2025-12-23 00:31:00 | METOP-C | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3fb7b73c-e9b2-3f61-937e-bc5630ff84ac | -21.4886 | -48.637299 | 2025-12-23 00:31:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d3ce40fc-9631-36e2-9ece-33955e3c4c3e | -20.8759 | -50.0658 | 2025-12-23 00:31:00 | METOP-C | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4aee1692-ccd9-3543-93f1-f362bc2ed9af | -1.4948 | -45.918201 | 2025-12-23 00:31:00 | METOP-C | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1f54840a-9682-33e7-8b76-edfefe86b19c | -20.688299 | -48.798698 | 2025-12-23 00:31:00 | METOP-C | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2986a03d-f07e-3ccb-8296-dbb47df4c8ae | -21.493401 | -48.6632 | 2025-12-23 00:31:00 | METOP-C | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 77513618-4c8b-38df-ac3d-f63cf2e46d7f | -21.490999 | -48.6502 | 2025-12-23 00:31:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3510218e-0da1-3960-8d38-8a03c1e5523e | -0.9378 | -46.906898 | 2025-12-23 00:31:00 | METOP-C | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a86b543b-b5ad-382f-8ea6-1255dac8f680 | -21.3766 | -48.633202 | 2025-12-23 00:31:00 | METOP-C | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5af7069a-4e43-344b-88d1-cc559d0f79dd | -21.5022 | -48.6492 | 2025-12-23 00:40:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 06359315-eb7b-37a7-8f69-fd3bf6d4daff | -21.5022 | -48.6492 | 2025-12-23 00:50:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a6c3a9b9-fa02-39e0-8882-26cca35b2c22 | -21.5022 | -48.6492 | 2025-12-23 01:00:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 1596cda0-40eb-3894-ae35-b3b60f19c3e7 | 4.3724 | -60.3404 | 2025-12-23 01:10:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 6db7d424-86ef-3716-a991-39ddc2bdbfdc | -21.5022 | -48.6492 | 2025-12-23 01:10:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 94.9 |
| fe5c2135-474a-3d76-aacf-da1658c58d9f | 3.511 | -60.8906 | 2025-12-23 01:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 38.2 |
| f8d7987b-d9b6-385b-8503-3856fdfdd19a | -21.5022 | -48.6492 | 2025-12-23 01:20:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 4f0d5995-2353-35d6-acbc-d42bef25421d | -9.7254 | -60.2071 | 2025-12-23 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 10249f1b-afaa-34f6-96a6-93e0ae348159 | -9.713 | -60.231499 | 2025-12-23 01:30:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f54e005-e932-3479-980a-dfdaae042031 | 3.511 | -60.8906 | 2025-12-23 01:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 31.8 |
| d74d9a19-3ad9-3ee2-88be-8f14de1cc845 | -9.7254 | -60.2071 | 2025-12-23 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 150c0b34-6edd-33cd-ad3a-dbbbf7172106 | -10.5744 | -36.8678 | 2025-12-23 01:50:00 | GOES-19 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| f8cc63c9-d298-318b-894c-b60757e003b7 | 3.511 | -60.8906 | 2025-12-23 01:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 06f09541-906b-3c3f-8b9f-2d0fc6c1c26a | -9.7254 | -60.2071 | 2025-12-23 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| f0a10332-86b5-303f-bf3c-e50bd7e7ec7c | -9.7254 | -60.2071 | 2025-12-23 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 90f02d72-fddb-3a1c-8fa3-980f05488e62 | -9.7254 | -60.2071 | 2025-12-23 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 036a5e6a-2cec-3558-b1e1-f20b609998f1 | -9.7254 | -60.2071 | 2025-12-23 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9c5f043e-022e-3bf5-942b-219013e27d0c | -9.7254 | -60.2071 | 2025-12-23 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| cc3b0ef9-dd67-3a8e-a57f-ebe62cdc3d44 | -9.7254 | -60.2071 | 2025-12-23 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 734735e8-efe8-3b4b-8689-0718b9861dee | -9.7254 | -60.2071 | 2025-12-23 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c2566f8c-df3b-3322-bfae-9bfe1f8183ef | -12.27875 | -43.55072 | 2025-12-23 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 22c61c05-7af0-3a5d-ba79-a6a6c0ab68d9 | -11.77961 | -38.72081 | 2025-12-23 03:25:00 | NOAA-21 | ÁGUA FRIA | BAHIA | Brasil | 2900405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3d5ddd87-55da-3417-9b00-20d380e36eed | -12.28487 | -43.55203 | 2025-12-23 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c6a3d868-4e8b-3378-8b56-5e7231556d05 | -16.83861 | -44.24754 | 2025-12-23 03:25:00 | NOAA-21 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1067a78e-419b-3910-b543-530f41c04d7b | -12.27777 | -43.55554 | 2025-12-23 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 291b3e8c-6803-3d3e-893c-c8a16613cd34 | -12.27165 | -43.55425 | 2025-12-23 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ed79c400-c205-3c4d-a977-41b9ffa844ce | -12.27262 | -43.54942 | 2025-12-23 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 32af347d-81b5-351f-a0ef-fbf6edf167b2 | -11.77876 | -38.72549 | 2025-12-23 03:25:00 | NOAA-21 | ÁGUA FRIA | BAHIA | Brasil | 2900405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 54a98738-2d3c-3f86-b962-1367b50eef71 | -12.27972 | -43.54589 | 2025-12-23 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ddc0c403-c624-3ada-84d4-02aa9515e802 | -21.49179 | -48.65291 | 2025-12-23 03:27:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 19e5110e-1de3-32d0-abb5-5d46ec19eb4d | -21.49855 | -48.65516 | 2025-12-23 03:27:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59c90c74-3c24-3243-9ad1-3a662bcc724a | -21.02111 | -48.67438 | 2025-12-23 03:27:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 09932a2f-276f-34f6-8f0a-2d9d30215c40 | -21.50038 | -48.6479 | 2025-12-23 03:27:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47a3b70c-93a7-3d11-8745-fc67e4135774 | -27.78435 | -50.28539 | 2025-12-23 03:29:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8078b73a-8f6a-3c99-9b9e-f5637161e184 | -9.7254 | -60.2071 | 2025-12-23 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 3a99e1c9-6ac4-3af0-851b-467e16edac2a | -9.7254 | -60.2071 | 2025-12-23 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 41bc484e-7efc-3447-a353-e3865e7e3598 | -1.49746 | -45.91531 | 2025-12-23 03:51:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0400a28-9d8e-3ccc-b798-c98cb4622cbe | -1.49683 | -45.91928 | 2025-12-23 03:51:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1985ca5b-e7b7-3ecc-a54b-d2afee376e6b | -11.77647 | -38.72206 | 2025-12-23 03:53:00 | NPP-375D | ÁGUA FRIA | BAHIA | Brasil | 2900405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 384b3d62-b32b-387e-8359-723eba9cfffc | -9.08382 | -40.09606 | 2025-12-23 03:53:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a04dfe10-9ba3-3f8d-b12b-2c2172f36f31 | -11.77981 | -38.72261 | 2025-12-23 03:53:00 | NPP-375D | ÁGUA FRIA | BAHIA | Brasil | 2900405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 92e3523b-590d-3b35-8f4d-5a59764896de | -11.14799 | -43.32589 | 2025-12-23 03:53:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 93be3b81-7103-3c75-8bc2-8f133dea1214 | -9.97569 | -37.03851 | 2025-12-23 03:53:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6bde27d4-b4b7-36a3-b4c4-a7e2a8a8cec9 | -13.65963 | -44.29965 | 2025-12-23 03:55:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d827bdb9-864e-31b2-8ad1-530835c5fbdc | -15.58749 | -41.76906 | 2025-12-23 03:55:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 78020c78-36b9-3cf0-b7a8-db5ca3f73614 | -13.66383 | -44.3004 | 2025-12-23 03:55:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26249064-bf76-32c3-bb06-4bab829abbbf | -17.31085 | -44.92822 | 2025-12-23 03:55:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8800ac09-6aca-30bd-9f7c-407238445225 | -16.24676 | -42.23136 | 2025-12-23 03:55:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bb14ba7a-485e-3b02-b2ba-d88975b526c7 | -16.25035 | -42.23198 | 2025-12-23 03:55:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bd8c4194-093b-3cfc-93b7-86419c86108b | -12.92105 | -39.6161 | 2025-12-23 03:55:00 | NPP-375D | ELÍSIO MEDRADO | BAHIA | Brasil | 2910305 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c1d710a4-b8a1-3b60-acc9-ccda7ca2ba77 | -22.43675 | -48.1973 | 2025-12-23 03:57:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbfdd795-8d39-3705-af77-8d0b62d9e252 | -21.49841 | -48.64951 | 2025-12-23 03:57:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 196714cf-dd99-3cc6-9d78-0d2672cde133 | -21.04748 | -49.58969 | 2025-12-23 03:57:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| e2789d7f-f5bb-3ddf-bfa1-5ee9a4461549 | -21.04833 | -49.58937 | 2025-12-23 03:57:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0b420282-8af0-38b0-be73-35e3c50b56f4 | -21.04759 | -49.59276 | 2025-12-23 03:57:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 0ff4fa45-92c3-346f-88be-c50bf540c5ea | -21.49245 | -48.65395 | 2025-12-23 03:57:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec7cca69-76dc-30d3-b2c6-9d9e66d7e542 | -21.04238 | -49.58841 | 2025-12-23 03:57:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0032ce38-073e-30ea-a083-b0f99239dda4 | -21.49721 | -48.65522 | 2025-12-23 03:57:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 35bed009-6098-3f4a-8aa4-4db7c59cf797 | -21.49364 | -48.64829 | 2025-12-23 03:57:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07074b4a-fb9c-32e4-aad5-3c88186b1351 | -21.04323 | -49.58807 | 2025-12-23 03:57:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5eedcd50-a5f5-3d10-9a76-ace9f6534af0 | -21.04676 | -49.59311 | 2025-12-23 03:57:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| b963c86d-65db-34f3-867d-c6582170669a | -20.87789 | -50.07378 | 2025-12-23 03:57:00 | NPP-375D | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4632045a-636b-3927-b93f-060b97d3aa79 | -20.69941 | -40.61015 | 2025-12-23 03:57:00 | NPP-375D | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b86f50b2-cccc-3f82-8e13-b9d55604caa4 | -21.04249 | -49.59147 | 2025-12-23 03:57:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| acb5570c-09ce-342a-b13b-fd69edbfdef4 | -19.26982 | -49.18958 | 2025-12-23 03:57:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 576698e5-f0e7-33fa-a2b4-dd1fa00e262f | -19.26467 | -49.18827 | 2025-12-23 03:57:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29944979-3e49-3217-a19f-b37109054031 | -21.04165 | -49.59183 | 2025-12-23 03:57:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 92aab1f0-b8c8-3ae8-b724-1a637215b515 | -20.85563 | -49.09442 | 2025-12-23 03:57:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8dd9fea0-2426-328a-a513-b838bbd5b8f3 | -20.69015 | -48.80075 | 2025-12-23 03:57:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 33eda7e4-bc59-3eb7-9829-ef3a10134707 | -20.87712 | -50.07729 | 2025-12-23 03:57:00 | NPP-375D | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ccfc4a8f-fbd2-3b42-a1e6-8b3a86386182 | -26.43424 | -51.04364 | 2025-12-23 03:59:00 | NPP-375D | MATOS COSTA | SANTA CATARINA | Brasil | 4210704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 229da1a2-2384-3288-8c1d-a14722df9ab2 | -27.78755 | -50.28706 | 2025-12-23 03:59:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7d2a4e63-a6b4-3536-a541-e243c3653616 | -26.43497 | -51.04042 | 2025-12-23 03:59:00 | NPP-375D | MATOS COSTA | SANTA CATARINA | Brasil | 4210704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d89139c2-a54d-3711-acd9-8e348ad5350d | -9.7254 | -60.2071 | 2025-12-23 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 3b0c51cf-87e6-3d19-9e3a-9169db8ab70c | -1.5025 | -45.91332 | 2025-12-23 04:14:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README2.md)
