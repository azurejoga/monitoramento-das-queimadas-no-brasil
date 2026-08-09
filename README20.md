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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cee4a99-68fe-32d4-85a2-1e0bad6d8771 | -14.02144 | -53.81606 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0e1aa80-d1d1-3c20-bcde-d766ee7989eb | -14.05067 | -53.84686 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ad5bbe8-6400-3bb3-b089-a0743b012600 | -13.84156 | -53.7041 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f15620e-a96f-3156-9575-ee6fb3b25cc4 | -13.86202 | -53.6766 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| edaff477-17e2-38a8-9f25-d2c36018fc46 | -14.1531 | -54.00948 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b512d04-7f5d-3e49-8573-8b32c31f1808 | -14.07049 | -53.82356 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 382b67d3-6c37-38fd-be51-84f5d839de7c | -14.90982 | -48.23684 | 2026-08-09 05:14:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ab9c6572-e596-3d14-9081-08f9fdb2fa46 | -13.87489 | -53.67458 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 91dee160-f629-34e0-a0c1-0fd7d175f8ca | -16.72004 | -54.76926 | 2026-08-09 05:14:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2b7c4a69-c93e-3482-97dc-fe4f419dae40 | -14.77833 | -56.36828 | 2026-08-09 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d3af1cbf-fd6f-3419-bd42-62e6d0da3612 | -14.32064 | -54.92089 | 2026-08-09 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fedaffe-28a2-35ef-9d14-1f3f3be3d320 | -18.63304 | -49.87164 | 2026-08-09 05:14:00 | NOAA-21 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6f1ed823-9574-38bd-834c-cf9fb648bfdc | -13.93933 | -58.12136 | 2026-08-09 05:14:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 83a890ad-6d77-38f1-a201-2e4fe91c51f6 | -14.06999 | -53.82724 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 776cc590-55e5-361e-9fd1-977812c8adfb | -14.31215 | -54.9543 | 2026-08-09 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a336ce32-0648-3df9-be28-c3e61e4adccd | -14.90935 | -48.24122 | 2026-08-09 05:14:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0a00fe37-228e-3879-95cd-eea040b2513a | -14.15665 | -54.01372 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 96e9f85b-b1e2-39bd-aef2-6a7b9b07abf9 | -21.98834 | -56.01779 | 2026-08-09 05:16:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0c1e3190-9a5c-33e2-b13e-93ee53b6a574 | -21.98662 | -56.01931 | 2026-08-09 05:16:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 52e2f2eb-da81-3868-b88a-1cbff757837c | -20.45693 | -57.40411 | 2026-08-09 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 205ee160-e153-3929-9420-ed3a181dc021 | -21.98725 | -56.0141 | 2026-08-09 05:16:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 03514bf0-84b0-329b-8766-f219932f4c31 | -20.78187 | -57.66819 | 2026-08-09 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 98915f02-680d-364b-ad28-5254379b3652 | -20.79555 | -57.70132 | 2026-08-09 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5e432340-e27b-381f-ac08-50afa66c04fb | -20.78779 | -57.70452 | 2026-08-09 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 895f4a20-40c7-3604-afea-c43d4b8c28a4 | -20.45331 | -57.40355 | 2026-08-09 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 58f855b9-fa42-3efe-82e1-375eae1f827e | -6.8388 | -56.4146 | 2026-08-09 05:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 70525507-e790-37e0-970f-d55a73a837c8 | -16.307 | -49.425 | 2026-08-09 05:20:00 | GOES-19 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 115.6 |
| be29115d-57f1-3119-8446-e87c6e93e4f6 | -6.8388 | -56.4146 | 2026-08-09 05:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 3a71d70c-b165-3469-a4db-8777944302a0 | 1.67959 | -60.13784 | 2026-08-09 05:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd0fd782-4f57-3683-b409-9b2dd600022d | 1.68027 | -60.13704 | 2026-08-09 05:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51a4867a-d02f-38a3-a2d3-0e3290f71042 | 1.65912 | -60.13657 | 2026-08-09 05:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a5de3c9-f7db-3733-b941-ceb95cff8db3 | -5.88421 | -57.64796 | 2026-08-09 05:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5187b48-49ce-37d1-8e84-e8bd92a1f08a | -4.96117 | -62.34481 | 2026-08-09 05:46:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48314b62-88b8-3356-bace-d826f17d44a8 | -6.14649 | -57.71866 | 2026-08-09 05:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a2346c87-c57c-32a1-8090-13a66e9b9d9a | -5.02935 | -56.12726 | 2026-08-09 05:46:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 476a7b0f-6d11-3703-a871-8761fc23dff5 | -5.03492 | -56.12249 | 2026-08-09 05:46:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf49f057-d54b-37bd-af85-640cdbd948b1 | -6.14587 | -57.7228 | 2026-08-09 05:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 516ad3bf-2f81-3281-8c5c-cd49ab7e3586 | -6.13779 | -57.71749 | 2026-08-09 05:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6d8ca74c-072e-3a57-a921-8f7de969d75b | -6.64631 | -56.43202 | 2026-08-09 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77df2136-750e-3f04-92e8-bcf0579e4a34 | -5.14426 | -62.51437 | 2026-08-09 05:46:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac56a974-15d5-35c0-8f8e-9cd139732ef9 | -3.02879 | -54.52451 | 2026-08-09 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f238117-ef21-3fd2-b1a7-c923da873e43 | -6.64546 | -56.43283 | 2026-08-09 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d11ffe7-92e5-372d-888a-1167ef7179df | -6.14214 | -57.71807 | 2026-08-09 05:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8bb93dd7-4b3e-304a-b6f2-15f4ba9d33fa | -6.65027 | -56.43336 | 2026-08-09 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f59e4b51-519e-36ec-b872-edd1b0bfb10c | -2.59864 | -59.45955 | 2026-08-09 05:46:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b67d8886-3428-3b2a-a3b6-b694414d746e | -6.13905 | -57.70911 | 2026-08-09 05:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86d80fc6-3a48-39fb-a265-5f86ccdeb0de | -6.14292 | -57.72071 | 2026-08-09 05:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f84615cf-e91b-3445-bc75-dc90b4f2d4d4 | -6.14151 | -57.72224 | 2026-08-09 05:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 13b9b575-7697-3c1a-9721-5f07daed3d34 | -3.0672 | -59.85173 | 2026-08-09 05:46:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29c66a64-39e6-3ab9-9fed-292acf38cec7 | -6.60658 | -56.36825 | 2026-08-09 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2809afdd-739a-3bc7-9f9c-7ffc564e33db | -5.0301 | -56.12212 | 2026-08-09 05:46:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13606772-e776-3b26-b26b-7bb4477a9c68 | -5.88856 | -57.64859 | 2026-08-09 05:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4443f04f-a640-33a0-9495-f62fc45ee337 | -6.41451 | -55.78663 | 2026-08-09 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 917b3efa-438d-339f-b268-3bd0c7ddf38f | -3.02833 | -54.52753 | 2026-08-09 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed308714-ba62-31ff-9124-a8773e7f054a | -6.4195 | -55.78735 | 2026-08-09 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c917aec-acd6-3854-bb5a-104bc8a69370 | -5.8836 | -57.65214 | 2026-08-09 05:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0c82304-c50d-3593-934f-66f97d32f641 | -6.13715 | -57.72169 | 2026-08-09 05:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3b83d146-596c-39d4-bb61-fa1d57f013ce | -4.29902 | -55.72361 | 2026-08-09 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a568b09-4e1a-3110-93ec-c5bffb48b356 | -6.4185 | -55.7922 | 2026-08-09 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3d6367c1-30a4-30c4-87cb-dd6e1dd00c38 | -3.11848 | -59.92838 | 2026-08-09 05:46:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c98eb3e-16cc-38c4-aa8b-e8872897cf95 | 0.9686 | -60.40908 | 2026-08-09 05:46:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47cce761-2624-375d-b3cf-1c4147c784f4 | -2.95998 | -49.26003 | 2026-08-09 05:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27900613-4371-3383-b1cd-5789a844b9cf | -6.14726 | -57.72134 | 2026-08-09 05:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8b12d289-bf96-3416-9360-dc29c180dd3f | -4.96173 | -62.34126 | 2026-08-09 05:46:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 000e85ab-4acd-3782-b428-e69f6d44866b | -6.60732 | -56.36309 | 2026-08-09 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b623e243-a493-35ea-a7f3-10db2ec93301 | -6.13856 | -57.72015 | 2026-08-09 05:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5ca8c38d-a58e-373a-8214-7a767c1a8733 | -6.41871 | -55.79312 | 2026-08-09 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b7b626c-def7-3193-9aae-37705ffb1afa | -2.95891 | -49.26721 | 2026-08-09 05:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1aa4d6a6-2a43-337c-96ca-c59ec7fd8d2c | -3.06356 | -59.85119 | 2026-08-09 05:46:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d511f13b-dfd2-3939-bed7-738004bd44d8 | -6.6122 | -56.36329 | 2026-08-09 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca663fa5-57cd-39a2-93da-fbbe7e71173d | -6.14351 | -57.71654 | 2026-08-09 05:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f44263e8-c205-3a94-a885-69cb30a6b808 | -4.22368 | -56.25679 | 2026-08-09 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94cd867e-03b5-31be-8345-d3b7c3e26f74 | -6.14786 | -57.71721 | 2026-08-09 05:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27a6f024-643b-34fe-8361-17045b43ce44 | -6.65113 | -56.43251 | 2026-08-09 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd4d542c-8c91-3eb3-9ecd-ad24b2c1a2b4 | -4.90448 | -62.303 | 2026-08-09 05:46:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b0794b5-c2f0-392c-a329-8fb08d5f311b | -8.67755 | -62.87107 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b009dc30-a34f-3144-b2c2-9f7587128394 | -6.706 | -58.94999 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f87beaa-da1d-328e-a608-4f718c253511 | -6.83785 | -56.42047 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| bd57c712-1125-36da-b676-688f5e4d3030 | -12.34589 | -53.15522 | 2026-08-09 05:48:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8201d25-a329-3710-a2e3-8c09fa4f64b5 | -7.55676 | -61.15805 | 2026-08-09 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab00bfa9-f975-338c-9dc0-5a063829532b | -12.3517 | -53.16131 | 2026-08-09 05:48:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e49db876-c6c9-3df7-bfe2-016513baa23f | -6.82904 | -56.41355 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e28e2ef4-162e-359f-b7b4-aa15b5c7b0db | -11.99576 | -60.5087 | 2026-08-09 05:48:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e1b9a62-1adc-3c3e-bd7c-1c83b1357d2e | -6.72134 | -58.9305 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e90833b-1b31-337c-b2f1-6cb60ed9c53f | -6.72093 | -58.9335 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ced7cb3-4322-3e98-bc4f-3b979b882976 | -6.8827 | -58.93267 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7fbec935-5670-3d3c-a837-f3485eae1dad | -8.68772 | -62.87266 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2beb80a3-778c-32e2-99a4-f5c0df841f4b | -6.83359 | -58.92895 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c378713-2e26-301d-87b9-e04466b24fd7 | -8.68829 | -62.86902 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 504a35aa-044a-3b7c-9842-f1fa98974925 | -6.84116 | -56.4315 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfbf748f-9394-3d83-abd0-4eea45657584 | -11.2847 | -53.94471 | 2026-08-09 05:48:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52306514-1480-3f43-951a-65f639996950 | -9.19405 | -65.87292 | 2026-08-09 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3ff521a-8626-366b-8b18-b3251830a497 | -8.68151 | -62.86796 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52fba58d-1472-3719-87ea-1741b2ee174e | -6.82124 | -56.43375 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2d8759b7-8fe2-3229-b538-d6bfcf460988 | -6.71059 | -58.94695 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5353111c-7a0a-3096-8ca6-fc8f0c76ba1b | -11.84486 | -56.94902 | 2026-08-09 05:48:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30fa9d1e-f6ca-361d-b074-00467a1e85fc | -11.28414 | -53.94937 | 2026-08-09 05:48:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6ccc1bf-1f8b-31ab-9ef3-910009a2969d | -6.89081 | -58.93384 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76e5eccc-a952-3b08-981e-cbe5217b8576 | -8.78868 | -64.21346 | 2026-08-09 05:48:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8063959d-2041-3660-b869-e00fb1f31731 | -8.15479 | -64.09125 | 2026-08-09 05:48:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README21.md)
