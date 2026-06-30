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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b93ce5b4-56f4-3a3f-ae54-b5dfd771f759 | -11.89676 | -57.12533 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 349c1620-b249-3278-9d27-bd0d15f57f9f | -11.87203 | -57.08722 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c383575a-ede5-3a34-a9e2-4f2d53529632 | -11.11079 | -54.14406 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b433145-d10d-3ae0-b09c-4c49d5d31ae4 | -13.25784 | -56.79474 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4fca43d-0c7c-372c-8785-501f969d3355 | -14.19929 | -57.43341 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1575a80d-df53-36df-a4d4-ba830703608c | -11.21514 | -54.33443 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9198c22-3314-3656-a29a-2da550170e2d | -11.21388 | -54.342 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d85f4d27-375b-3bfc-97e0-15913e307034 | -12.2218 | -56.56092 | 2026-06-30 04:57:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 515a0266-fe34-3353-aaa5-f5a3da4f096f | -18.24704 | -53.85104 | 2026-06-30 04:57:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b92e37ad-2819-3ae7-a23b-35bc6c33bab5 | -13.71999 | -47.86142 | 2026-06-30 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d904c9a7-4338-3d52-ab9d-af5613cc3b83 | -14.27748 | -47.41666 | 2026-06-30 04:57:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50fc5922-01f9-3fa3-a25a-a52f4fa101a9 | -12.0499 | -55.45518 | 2026-06-30 04:57:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 392a2a0a-24fd-3a91-9332-e4e29fe0ef61 | -11.93795 | -57.70932 | 2026-06-30 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a670a7c0-e909-39a0-a4dd-3f37f4df9891 | -11.22516 | -54.31664 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e37fe9f-83c0-3076-86c4-14bcdaba6e85 | -12.51537 | -48.28061 | 2026-06-30 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0748f9b0-bf2f-352d-8fc6-863c8b590c6b | -18.24096 | -53.84626 | 2026-06-30 04:57:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 159596bf-03f4-3733-b647-303d6b56c60f | -13.26233 | -56.78808 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f98391f-2be9-3b7c-8dbe-d5df1d51e751 | -12.85289 | -44.40017 | 2026-06-30 04:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21e66a8c-1347-3284-93ef-d8a5ec54deb3 | -12.52171 | -48.29153 | 2026-06-30 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8bf7ed00-5005-3c67-9281-71ea844322a0 | -11.90369 | -57.13175 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bab6bd6-035b-3d34-979d-9ed4807ea3bd | -18.24819 | -53.84377 | 2026-06-30 04:57:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cc3ec6b7-d9ad-3ffe-b5f2-4a50bba1af04 | -11.52476 | -54.25723 | 2026-06-30 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fabb4212-c057-32fc-8c6e-2527be156eed | -13.71403 | -47.8749 | 2026-06-30 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2a963cf-e41f-360b-821b-04071f28317b | -11.88635 | -57.12098 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14e6cbf3-b4a2-370f-b300-fed160380f84 | -11.10945 | -54.14678 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a67186ed-2c43-3b94-883b-086ef7a07624 | -12.44948 | -58.50044 | 2026-06-30 04:57:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5129a6c1-336d-3470-886f-ac0535f730b1 | -11.95807 | -58.61508 | 2026-06-30 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1f85d9c-b57f-38f8-9cc7-d2df9cd789a9 | -11.22797 | -54.32101 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0fbf169c-fa47-32e2-80a5-fb4f21256ad4 | -12.20902 | -52.86702 | 2026-06-30 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8596a4ad-7485-35e4-ba70-dd8aa35c448d | -12.85976 | -44.34729 | 2026-06-30 04:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 229e9ab4-7019-3c2d-a9d9-64db70414462 | -17.59815 | -52.49666 | 2026-06-30 04:57:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95f483bb-5196-36b5-834e-988dce55947a | -10.9046 | -56.85728 | 2026-06-30 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c890c29-0161-37e2-bd4b-541d6c5d0cbb | -10.85413 | -56.66362 | 2026-06-30 04:57:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08808b66-e43f-3e25-b01f-7d953729f1fa | -11.89896 | -57.11803 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7527dd89-5a2e-3aa8-ae08-41cc62deef8d | -11.90045 | -57.37929 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 42756681-1ae6-3c49-bc6c-9c5770183a9a | -12.21524 | -56.55767 | 2026-06-30 04:57:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 28e34782-798f-3ee7-9ffd-1303e9ccc32c | -11.89246 | -57.13236 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b48ad752-3b8d-338b-97ca-e177209c6f3c | -10.55359 | -56.33682 | 2026-06-30 04:57:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5784c680-b0d6-3869-84d4-cda2b72fa639 | -13.71644 | -47.85723 | 2026-06-30 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2301bc84-5f90-3765-9bb8-c8f137189dc9 | -12.22279 | -56.55898 | 2026-06-30 04:57:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e9b9d2d4-fe41-3b87-84ce-6886857b4454 | -12.60986 | -57.89182 | 2026-06-30 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45ec6d48-72ea-3c04-a436-85dcdadf43be | -13.26754 | -56.80616 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 01ba16c7-f4f1-326a-9ae1-ae42173f5767 | -11.8981 | -57.12304 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8aeea279-d847-3ffb-a866-602104ce936a | -10.24637 | -59.3036 | 2026-06-30 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28b71ca9-eefa-3d61-b81d-0b44ea37b84f | -12.45519 | -58.4931 | 2026-06-30 04:57:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9d2f94ca-8033-3a03-8ee7-b4772a32d85d | -18.50575 | -51.66378 | 2026-06-30 04:57:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6e7772cd-d179-39ae-af85-306b13123742 | -13.94446 | -53.95085 | 2026-06-30 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad4be892-17ac-3b78-8dc7-4dedd45ff660 | -11.11018 | -54.14781 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c23a455c-34bc-3641-96f1-0d318207b31b | -11.88941 | -57.12664 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f8bd9f9-95d4-387e-ab50-3a7b452ecb0b | -13.26002 | -56.80468 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0b255a06-5936-3ee1-b3db-cd77fbeec810 | -11.11007 | -54.14303 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dc2d727-228e-39c6-bb46-10eb81c299e8 | -12.66992 | -56.38605 | 2026-06-30 04:57:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f2ab7a0-9c91-3af5-a45e-7a46ab9d0ce5 | -13.24015 | -51.55888 | 2026-06-30 04:57:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8687cc2-2dbe-32fe-a0aa-8ec2ed882484 | -11.90189 | -57.14185 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b515ee8d-1745-3f3f-a7a4-6d0d1e5431c6 | -13.23958 | -51.56253 | 2026-06-30 04:57:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b02eda7-9b8e-3c9d-b87a-e66207ef27bf | -10.04656 | -59.10935 | 2026-06-30 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c76c541-1164-31d0-aded-c3b4e820bfac | -16.17537 | -59.34395 | 2026-06-30 04:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4734d786-cf1c-3325-b68b-07cb84b54880 | -18.24153 | -53.84262 | 2026-06-30 04:57:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb26e17c-e6e3-3f9d-8755-7f265fd51106 | -17.70586 | -46.78698 | 2026-06-30 04:57:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8190195a-7d75-33da-bb6e-855ba99f5a53 | -12.5122 | -48.27511 | 2026-06-30 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ef93d377-7d26-3e75-be55-17246de68e93 | -11.79479 | -56.99924 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c19cc960-0246-3beb-9931-28d38857c083 | -11.3771 | -55.80968 | 2026-06-30 04:57:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e9638f3-ba5a-3f64-b52f-7ff776cb95f2 | -12.85194 | -44.36027 | 2026-06-30 04:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bb1fdf4-4bc7-3873-b3d5-067471fed4f5 | -17.44243 | -47.16145 | 2026-06-30 04:57:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0e5e1110-5076-314c-b083-3d4f9b3dc34a | -14.63023 | -54.45994 | 2026-06-30 04:57:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c2053e3-8bcd-3c71-a003-1438325cced0 | -13.93222 | -53.94135 | 2026-06-30 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aeda36f0-96c1-3a5e-b462-49be525a2fe8 | -13.69838 | -47.86894 | 2026-06-30 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09975316-9561-3768-9925-fcddcba1f211 | -11.31061 | -53.94705 | 2026-06-30 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e8855cc-2836-3eb4-953d-90db3d29b734 | -11.93325 | -57.7122 | 2026-06-30 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 939b6eac-cbd4-347e-a577-5876e7a7c039 | -12.45022 | -58.49638 | 2026-06-30 04:57:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4ca527f3-c44c-3517-8c88-e0113ea19db9 | -13.2624 | -56.7908 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f3f72a0-e021-379a-b3bf-8454a5a1c84f | -11.52209 | -54.25759 | 2026-06-30 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70939e93-8966-3d84-b909-2f2f0a116a49 | -11.90334 | -57.13956 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfd3134f-f929-35da-b98d-96f680e69702 | -12.28624 | -57.55481 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5be76a7-bf4a-3453-a1be-3e0bbfa594f9 | -14.27705 | -47.41802 | 2026-06-30 04:57:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 704503b2-d0e2-3559-a1cd-dd9b4bc97831 | -10.72354 | -56.22981 | 2026-06-30 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2908c086-4959-3060-a00c-cd290a271016 | -11.87115 | -57.09225 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53f1405e-e130-3fec-a1d4-e6327994b8aa | -15.07161 | -55.81221 | 2026-06-30 04:57:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0a30c09-47c6-3e5d-8cf6-58e6432ec938 | -11.89765 | -57.12035 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21f1cdcc-2f9c-3454-8cbc-b61b6bc43ba7 | -11.22235 | -54.31227 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c3f1b2d-683f-3347-a178-89e2c859c91f | -12.61457 | -57.8889 | 2026-06-30 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 615e099f-27ab-3748-9026-ec3ddb6bf6f3 | -12.44525 | -58.49963 | 2026-06-30 04:57:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a16906d8-9437-3f26-944e-3becae538333 | -12.60238 | -57.88669 | 2026-06-30 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55ba9f6d-bdd0-3975-8457-e7a986000f4b | -15.07583 | -55.80872 | 2026-06-30 04:57:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34c2d3e9-72b6-35af-b5d6-967a22c6d6a9 | -12.20569 | -52.86647 | 2026-06-30 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 83fdd790-784d-3910-99b7-eeb8e3e52e6b | -11.9326 | -57.71584 | 2026-06-30 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fcdf660-9323-39a0-a567-e7ce7601b58a | -11.9339 | -57.70858 | 2026-06-30 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e392ef7-da7f-3953-9af5-0826e8e0a127 | -14.19758 | -57.44313 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c13a648e-4776-3c0c-855b-964b0aa77a06 | -17.71043 | -46.78775 | 2026-06-30 04:57:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 31a230ea-7791-3e9d-be2f-33fd6ccf5f8e | -11.23204 | -54.3178 | 2026-06-30 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c18b2e3d-aacf-392d-bd83-72608a06deb2 | -13.69793 | -47.87229 | 2026-06-30 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5450c2f4-8b1e-3242-8a48-106ae9f5735c | -11.92157 | -57.39923 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecfa542d-b5f6-34d1-b533-4515971103cc | -11.89888 | -57.41144 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 709aa6e1-6b34-3fce-8fa7-694e31cac163 | -12.21902 | -56.55832 | 2026-06-30 04:57:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8f41a265-222c-3273-8fe1-a2b02dbeaf61 | -12.21603 | -56.55306 | 2026-06-30 04:57:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1edb1fb1-3485-3171-a255-6d4617a087c0 | -12.85268 | -44.39622 | 2026-06-30 04:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 18605fd1-c75f-3417-b628-6fdb6654ff45 | -11.89978 | -57.13104 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d849977-e370-3725-8b30-1d8e054d4751 | -13.26151 | -56.79269 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0a6dca5-35c5-358e-852a-6423e4badf1e | -11.90287 | -57.41212 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d50b2c7e-934c-3ef4-8223-b0c3172008ae | -16.1973 | -59.31974 | 2026-06-30 04:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README13.md)
