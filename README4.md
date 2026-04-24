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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e499f658-b48d-35d0-b369-88712e0deb3d | -11.3002 | -54.0191 | 2026-04-24 04:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 970ccc96-a793-3ced-ab4c-bfc2073205b0 | -12.98339 | -54.6856 | 2026-04-24 04:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f50a5727-d2b7-3616-8e3e-e7dbefe06c22 | -13.54895 | -47.89672 | 2026-04-24 04:29:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7879a240-fd8f-36da-9f31-41d378871d44 | -13.38236 | -45.31644 | 2026-04-24 04:29:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98f0cc4d-38d9-39b3-88c6-24003812f873 | -13.37945 | -45.31191 | 2026-04-24 04:29:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5123fef5-349b-3eda-bbaa-7d951e13dd02 | -13.37885 | -45.3159 | 2026-04-24 04:29:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 027abb8d-564b-38f9-a3fe-ca77599a78de | -12.65474 | -44.52854 | 2026-04-24 04:29:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b90b5f2-8807-3496-be79-0255c803b24b | -12.65619 | -44.5272 | 2026-04-24 04:29:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df52c653-fec9-3f73-a5ab-dec8ad9b73bd | -13.49183 | -48.91411 | 2026-04-24 04:29:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58deba0e-fd87-34ac-b20d-97dab3dbe8e5 | -12.08948 | -51.22516 | 2026-04-24 04:29:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 673c88df-471b-3aa8-9977-6c5fb0af0d86 | -11.85046 | -55.01653 | 2026-04-24 04:29:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 522018a7-3f93-3a83-9a96-b79844ba3c38 | -14.34159 | -47.23393 | 2026-04-24 04:29:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5bb8095-6140-3c24-a1e0-6055590ed741 | -13.37594 | -45.31137 | 2026-04-24 04:29:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa583aa1-99c4-323b-8adb-7ca25170d1b7 | -11.91228 | -58.07018 | 2026-04-24 04:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34a09f5d-0912-380d-8c01-dc3004e76af0 | -11.94004 | -58.08044 | 2026-04-24 04:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16e73cdb-e0fc-3072-82bd-b42be66b1096 | -12.2787 | -44.62537 | 2026-04-24 04:29:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc842332-8c69-3ab4-899f-0be43883db2d | -12.09241 | -51.23024 | 2026-04-24 04:29:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e9e0ea4-37a3-351c-b2e9-aef372005415 | -13.38004 | -45.30792 | 2026-04-24 04:29:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3170d10-47fe-35a5-bfc6-d8e68fe0d4ee | -14.74795 | -42.46196 | 2026-04-24 04:29:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab065452-4e30-3ec9-81e2-c5ac1e3d4463 | -10.97648 | -49.43042 | 2026-04-24 04:29:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fa27039-7e0f-3d06-a5f5-707db0f6f9d9 | -13.54675 | -47.88911 | 2026-04-24 04:29:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13e45d37-1a7e-3962-9c67-139c0c99d2ff | -11.93925 | -58.08451 | 2026-04-24 04:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5128c9d-c38f-315f-a293-f0771c0c0127 | -11.64396 | -52.56526 | 2026-04-24 04:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68f2a944-4cb3-38a5-b5c8-bc948e549c22 | -14.5934 | -47.97047 | 2026-04-24 04:29:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 810a9e7d-0455-3273-88b4-fabd2e0c84db | -9.23202 | -46.65187 | 2026-04-24 04:29:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd6b7f7c-1a36-3164-9a29-a0f524e08361 | -9.23257 | -46.64838 | 2026-04-24 04:29:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c701c4a-a6c8-3ee2-9705-fd691d704ce6 | -10.00641 | -48.66955 | 2026-04-24 04:29:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab55a4a6-b7f3-350a-9c20-80aae656bf16 | -12.54773 | -54.6153 | 2026-04-24 04:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aee39dd1-ea2c-3d78-b2e8-5f01ed8e97ff | -13.37244 | -45.31084 | 2026-04-24 04:29:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd9af1af-e293-3caf-ac4b-a36adb6f4a38 | -11.60076 | -55.32841 | 2026-04-24 04:29:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2909e58-726e-31f0-b743-5681bddc3fcf | -12.09317 | -51.22582 | 2026-04-24 04:29:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38e35101-472c-3481-91c7-1d0e12c23b62 | -12.28227 | -44.6259 | 2026-04-24 04:29:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71e0ee72-eedb-3fc7-b699-7f68ca7b36e8 | -13.55006 | -47.88966 | 2026-04-24 04:29:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc4c7dff-bce5-38c1-a310-0b97a90a4342 | -20.67631 | -48.96421 | 2026-04-24 04:32:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 54fdb4c1-cbba-3ab4-aa1e-bdad44d7d23e | -21.21857 | -48.61407 | 2026-04-24 04:32:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d7ab1491-fdcc-3235-9915-f7d07549ca62 | -20.19579 | -46.75253 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 754f05bc-c4f7-3084-90c9-8a6d98d44cab | -20.16158 | -46.86629 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a01d1921-6b63-3778-a013-aae74fac1f78 | -21.2055 | -44.20782 | 2026-04-24 04:32:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 578c4a23-e76a-3f47-9f5f-6d5c26a0d37b | -20.18876 | -46.72589 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70786484-cae3-3679-8b85-e531c7a82635 | -17.16598 | -46.834 | 2026-04-24 04:32:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6a94b9e-69a6-3494-940c-7bba77814f84 | -21.18719 | -48.63968 | 2026-04-24 04:32:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ef10a621-b41d-36f0-b77a-b0db6efb144d | -20.20903 | -46.81072 | 2026-04-24 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96ad484c-86ea-3632-8abd-52f03a71faf3 | -13.71028 | -57.48111 | 2026-04-24 04:32:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3432f2a9-8723-3b5f-8499-6bb2bd36ecf1 | -20.41479 | -45.19509 | 2026-04-24 04:32:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 86227296-b446-3dac-8a4e-5e9166f78061 | -16.70783 | -44.9567 | 2026-04-24 04:32:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fec11dd-2257-3e3d-acd7-91b7c348be7b | -18.28115 | -52.91799 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06e78800-bab6-3e55-ade1-aca2def46bcc | -17.50061 | -45.00682 | 2026-04-24 04:32:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 669afaf5-1777-33d9-b9de-b5ae1b8be0e8 | -18.29264 | -52.93938 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b72a798b-2c8f-374f-939e-adce22b44d86 | -13.7156 | -57.48227 | 2026-04-24 04:32:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68a92f6e-8eec-3223-9e46-dcd2fb9b3fdf | -20.19172 | -46.7305 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85d0a0d3-6605-3d96-a57f-e90d6bef1d50 | -18.27059 | -52.90406 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b1acbf79-9187-3d70-a2f2-ff99e6c8bbe8 | -18.26641 | -52.88425 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efccc2f0-f3bb-30b1-854a-f60142d16ab6 | -20.23546 | -46.75324 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fef18d9-6112-382a-a10f-64f3f7f53714 | -19.44036 | -56.57744 | 2026-04-24 04:32:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1567f3f5-c19e-366d-b1a4-7f507ea69779 | -15.96559 | -51.36627 | 2026-04-24 04:32:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78af7111-aacf-37ac-9f53-0fd2352ff031 | -21.63396 | -41.27073 | 2026-04-24 04:32:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 54392ee7-1c09-3eb1-8d75-2f4d7eaffd40 | -16.9085 | -49.30413 | 2026-04-24 04:32:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e51129f1-0770-34fe-b7fa-59826068b890 | -20.16569 | -46.86261 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53f8b773-c9d2-3fbf-8f50-d322045ebc82 | -20.21314 | -46.80713 | 2026-04-24 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d33d1ed2-f65e-3d45-aa6e-9cf24c58018d | -20.23841 | -46.75795 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71d3abb2-2c75-36c9-b69f-f7fa799f63eb | -20.20248 | -46.88103 | 2026-04-24 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b7dfe8b-dfc7-3c3a-b3c5-3c280a16e8bb | -22.26124 | -48.47569 | 2026-04-24 04:32:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd57a0ca-eaf5-3145-b9a1-5cb46219c22a | -20.19543 | -46.88021 | 2026-04-24 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bedadcc8-385e-382c-8e5e-a5fbae89ab99 | -21.6966 | -48.43514 | 2026-04-24 04:32:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8be22038-fe59-3c50-b503-b2a8f935a707 | -18.29552 | -52.94476 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 300d6f8a-dc38-3bb1-8c50-ebdb9aea5a2f | -21.0556 | -49.08226 | 2026-04-24 04:32:00 | NOAA-20 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ce18db31-2c41-3331-ac68-c7ec4a9322eb | -20.17722 | -46.95685 | 2026-04-24 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 104a0d84-b3e5-3d25-a83c-1a7b597cd113 | -21.58575 | -41.9332 | 2026-04-24 04:32:00 | NOAA-20 | CAMBUCI | RIO DE JANEIRO | Brasil | 3300902 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0f89a8b1-56c3-3de7-9598-ff2c767e90f5 | -20.19231 | -46.72631 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50340d0b-7a08-39bf-a605-9cbf1eff61ff | -18.30331 | -52.96555 | 2026-04-24 04:32:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ca7ff2b-20a2-3502-84ac-f497651d5d34 | -20.161 | -46.87037 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 28f2fa3b-303f-30a3-a65c-0c163c9aa4a0 | -20.17021 | -46.93098 | 2026-04-24 04:32:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dca96e5a-7780-35a0-9c65-8e22b0bb1641 | -20.71807 | -55.17244 | 2026-04-24 04:32:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d5565fd-8310-33f4-bce2-66ba73516a7e | -20.53251 | -54.62141 | 2026-04-24 04:32:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72dc55b4-60f4-3b4e-ae4c-d52603b5fa8b | -20.16276 | -46.85804 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00745067-8843-30e6-b455-064ba0a9d83e | -20.17373 | -46.93143 | 2026-04-24 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10fc3330-bdef-33cd-82cb-a29362aab906 | -20.20672 | -46.80177 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53f8c7f1-a334-3ecc-a2de-33fac1e77dff | -20.25067 | -46.77328 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8857593f-d933-3bed-84ba-eb8f30c3c09b | -20.24714 | -46.77282 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fef82e37-5a3d-3752-ae9a-bb19b2a4ccf7 | -19.44608 | -56.61943 | 2026-04-24 04:32:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1a09aeab-9bff-319f-ae7f-ebeea7240b39 | -19.45061 | -56.62045 | 2026-04-24 04:32:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 87b55bd7-201b-3ac0-8f62-d69e7cb4577e | -18.22625 | -54.59403 | 2026-04-24 04:32:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cd3cebe-3201-3d41-8a56-4a083463519a | -20.67688 | -48.9605 | 2026-04-24 04:32:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f53c269d-2f98-3635-bf62-b591c12f9648 | -21.06536 | -48.59223 | 2026-04-24 04:32:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 47a33a72-b414-3c5d-880a-701c219ae80f | -20.19957 | -46.87636 | 2026-04-24 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b848fe88-9788-30d5-b34f-f2a27022e5c9 | -18.29181 | -52.94403 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3dedc8bb-d081-336a-b8ed-c55e6cdeb8f3 | -17.53167 | -44.75241 | 2026-04-24 04:32:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| de2ccaae-c093-30df-b7eb-19f5258712bc | -20.21255 | -46.81121 | 2026-04-24 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 350228b5-cea1-3938-a5b5-c133f0210ef6 | -16.42488 | -54.92342 | 2026-04-24 04:32:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aee54710-f1d8-3d8e-ac30-2ed96f52287c | -16.42142 | -54.9181 | 2026-04-24 04:32:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 28468657-0ea5-38e9-8d3c-16561b9a2d34 | -18.27828 | -52.91265 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b7697b2-5612-33f8-ad1e-caf4423aef17 | -20.20612 | -46.80598 | 2026-04-24 04:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f19f5017-e2e9-35b1-bec3-53a41a7e9f5f | -21.69775 | -48.42746 | 2026-04-24 04:32:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c121ceaa-81f0-33f6-9dc5-35ff0e522415 | -16.42572 | -54.91899 | 2026-04-24 04:32:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 65176741-ffee-31ff-be28-730104dde518 | -17.26285 | -51.88228 | 2026-04-24 04:32:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9dc3fc85-2a5f-36d6-993d-dff43b25b54b | -18.29468 | -52.94939 | 2026-04-24 04:32:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65bad783-8b6c-3b28-b92e-ebb9b05f2dd4 | -15.3312 | -43.80424 | 2026-04-24 04:32:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc265e84-e6d6-3525-b800-fca32ecbfd3a | -20.19605 | -46.92557 | 2026-04-24 04:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d5fe1bd7-2cee-31a8-9c1e-f5a8344a083d | -17.49998 | -45.01147 | 2026-04-24 04:32:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62be41f4-f62d-3b48-bf25-7bb9a2b0291a | -19.79875 | -44.63512 | 2026-04-24 04:32:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README5.md)
