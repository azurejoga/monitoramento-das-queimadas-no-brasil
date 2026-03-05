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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb4627cd-0204-3220-8344-49e2cfe3c90d | 3.06422 | -60.62823 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f4ee4f8-6a40-3dc6-b366-98627d2157e3 | 2.69677 | -60.69157 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ae64039b-594e-3759-8aae-d277af657b2e | 0.04275 | -60.97355 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c56764c-16a0-3ca4-a3e4-9333082ea819 | 2.78254 | -60.3396 | 2026-03-05 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 41.0 |
| b66737df-063f-3cfe-b662-4000a8981d88 | 0.47356 | -60.32336 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d0a79a96-ee10-3d8f-a078-25e5c8676211 | 0.30396 | -60.45903 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dd510c67-f836-330c-82f4-600118f0e09f | 1.17429 | -60.36823 | 2026-03-05 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec42cb57-7358-3019-b850-771061968526 | 0.04041 | -60.98664 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bd75089-557d-3c61-8276-ac029ac1bdb0 | 3.28493 | -60.72961 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e395f9fd-b64a-3905-aab8-8b8c75e1a163 | 0.47624 | -60.32596 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 77b4fcca-460d-3db3-91ed-f130c164e900 | 0.58259 | -59.84239 | 2026-03-05 05:54:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ced1b0b-7454-3fa2-9ecd-25c95850e720 | 0.03477 | -60.97915 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8346fb6-16bb-3b37-940d-738a6c7f4b44 | 0.04328 | -60.98852 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bc4ca06-7eb5-3695-8214-428c1917a0ad | 1.51083 | -59.90992 | 2026-03-05 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f35064d7-5e9c-3c86-a7f5-38bba99c6cd4 | 0.47425 | -60.32786 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c2c0bee9-f088-35b9-8e49-59da3df21c84 | 1.51157 | -59.91446 | 2026-03-05 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5806ae4-c726-331c-ad9d-5b6abfe7dd2d | 1.02342 | -59.48401 | 2026-03-05 05:54:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4934a54b-48a7-3084-ba61-c522fdd4f8f0 | 3.18913 | -60.56789 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e7b8504-1686-33a1-870c-6b6fbb4b9e04 | 1.0628 | -59.48794 | 2026-03-05 05:54:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ecf55ce-1591-3348-824d-947fec5a0336 | 0.03707 | -60.97687 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba2a0042-56c5-30d0-a5ea-ec2631c5c800 | 2.66335 | -60.40918 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14b07be9-0ff4-3540-8f86-d75f813e1ab5 | 0.73271 | -59.9029 | 2026-03-05 05:54:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a41a1783-e80b-3cf4-af45-fb36cc21e8f5 | 2.77889 | -60.34444 | 2026-03-05 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 4f25bffc-73d0-39e6-944d-f99199676a58 | 2.78051 | -60.32714 | 2026-03-05 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 99e22413-1a14-3f43-a8bb-511bf2926a8a | 3.06908 | -60.63147 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c1955de-a9a5-3075-b1f6-d503d71b3ef8 | 2.7228 | -60.66451 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1f5f4b2b-bb1e-33bb-b8b6-11fa1885c2da | 3.28138 | -60.73417 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8f284029-d7e1-317a-b5a3-a0fd1fcf3dd4 | 3.06972 | -60.6354 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91952235-2101-358a-8643-efe35ba2a5dd | 3.02554 | -60.11372 | 2026-03-05 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0e9d161-8be7-3ade-82d5-7d176151a82d | 3.28682 | -60.74116 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbd12878-9d5d-3fc8-a848-29e4f864ad09 | 2.95479 | -61.08537 | 2026-03-05 05:54:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d2ff286-5178-38b1-90af-8c01aafc3b64 | 0.49599 | -60.50486 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccdc0638-0aaa-34a7-bd5a-293eb896e1f3 | 1.49476 | -59.93268 | 2026-03-05 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c2fb8ed-63a6-398b-886d-abb212eb92b7 | 2.96358 | -61.0877 | 2026-03-05 05:54:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 30c03873-2bf2-3046-bacf-f96dffc4c60b | 3.16925 | -60.24033 | 2026-03-05 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0dce34a8-8090-366e-bb19-9ac79bf4ca97 | 2.92229 | -60.44926 | 2026-03-05 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86f64a93-e4a6-3c4d-b902-bf3476e73ee7 | 2.97182 | -61.03315 | 2026-03-05 05:54:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db68ab1c-bc59-3d69-b971-35406643a200 | 2.78755 | -60.34303 | 2026-03-05 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 41.0 |
| a5add3c9-7776-30ec-8782-0329c4f7f653 | 3.02964 | -60.81995 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55de37dc-88d1-360c-82ff-47a351227a6c | 0.0377 | -60.98101 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39288a60-80c5-3f10-84bf-a82a3ad69999 | 0.4889 | -60.51217 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae37eb61-95d9-314e-a33a-30da48a2b393 | 2.22598 | -60.22428 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 38ac644f-fb95-3ad5-a255-5c4828cd7305 | 1.14981 | -60.89477 | 2026-03-05 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fadcc52a-9171-3c2e-a2a1-469005b5ea7d | 0.47287 | -60.31884 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1cd3c739-ceac-3c7b-bc9a-637c7bbf84e9 | 3.18002 | -60.56532 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8bfe48ff-344e-340a-876d-3b8a9aa203f7 | 1.00303 | -59.50776 | 2026-03-05 05:54:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b426be7e-ba2a-3895-819a-f8760f3c6f85 | 0.46221 | -60.39876 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32df4316-d0c3-3124-92eb-8059a37b448b | 0.49267 | -60.50711 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bad22706-f15e-3e52-8a10-15ba4b1c8b77 | 0.66373 | -60.30297 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3be70a6c-1aa9-3caa-8a8b-e8cb084ece21 | 2.72409 | -60.67241 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4713d87d-3c75-3fb6-91ed-4a61e51fd967 | 0.05276 | -60.98071 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30181470-2f9e-335b-85ec-caa1662d2af0 | 2.97499 | -61.03394 | 2026-03-05 05:54:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| de2415d6-7241-35e9-bb25-482e6343a21c | 3.2843 | -60.72578 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 42ba9d78-2eb8-3f00-98d7-8785a6f0810c | 2.71986 | -60.6731 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce549fd6-fcd9-3f5f-b528-94532a123c41 | 2.96124 | -61.09944 | 2026-03-05 05:54:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6cc2f15-a42b-3d1a-8a05-ae7031820ebd | 3.50797 | -61.90388 | 2026-03-05 05:54:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2eeb835d-4ff8-3dff-b43d-ce7702a5534b | 0.04775 | -60.97706 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06aef05c-5db6-3714-8b20-2a16d85a70b4 | 0.04076 | -60.97196 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64ecc856-a273-308e-b449-160fa96cb7ce | 2.72215 | -60.66056 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53ec7141-ea49-3fc6-b965-ca0ad63bc2a4 | 0.67667 | -60.53169 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ee1447c-1e44-309d-9ac0-0ee54c1b0355 | 0.49335 | -60.5115 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d80888c-92a9-31b7-b422-472a8837695c | 2.69316 | -60.6962 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a5640836-89d6-3b29-b40a-40021e6d28bc | 3.28241 | -60.7142 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aec2f644-b81f-3fe9-bda5-741f90fdfa24 | 0.96928 | -60.52631 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 531dd174-2509-3074-a846-f0ce5ecdb2f3 | 3.02297 | -60.64182 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f349df4-76fe-3f89-936b-4b0b1acb94cc | 0.7281 | -59.90366 | 2026-03-05 05:54:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 598391ab-e0c5-3aa4-94b4-c90eed9ba517 | 2.69673 | -60.66471 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fa3062f-4d31-34a1-8bba-37a77d5c3ed4 | 3.06358 | -60.62429 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c982153e-eda7-3ac3-af08-9e28d0c71d00 | 3.0273 | -60.83214 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5cfc5af4-2036-3060-a1a3-d2700df87e8b | 2.97316 | -61.0228 | 2026-03-05 05:54:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c7c0e6e-568b-3772-b3c9-9ee618a1e23d | 2.70684 | -60.64679 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d840ec4b-e235-3110-baf3-520c579dbd79 | 2.70038 | -60.68693 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7ff84178-6220-32a6-8c5f-adbde26aa037 | 1.36084 | -60.37771 | 2026-03-05 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d310f96a-2e4d-338a-a049-7d61099320f1 | 3.02312 | -60.83279 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a4797403-84b8-3090-8995-3dbc1a4e4f60 | 3.28201 | -60.738 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb6a7756-8453-33e3-8c47-5cd38157f185 | 2.2253 | -60.22007 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15d5de3c-7d9e-3563-9efc-6440964bf0af | 2.78822 | -60.34715 | 2026-03-05 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6a4e93f3-5392-3d26-a047-d779a5b102dc | 2.96476 | -61.09508 | 2026-03-05 05:54:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e08bbc3b-7570-3227-9c61-4de34a29db7c | 2.97418 | -61.02131 | 2026-03-05 05:54:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9d01ce7-fb5e-3d9e-9d19-95c803b031d4 | 2.72344 | -60.66846 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 12c5be21-8694-3f5b-8b90-25e77b2b3268 | 2.69249 | -60.66541 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 615f6f6a-c5bc-3f36-8280-c66df11ae781 | 2.78687 | -60.33892 | 2026-03-05 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 41.0 |
| ede90cff-77a1-38bc-95bc-f090e03f7809 | 3.03043 | -60.63381 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c0d4e34-e01b-3344-a9e9-b7af8b02b98e | 0.03738 | -60.99544 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0811b23b-dba2-31e4-b88e-0c6a2533c5c5 | 0.04203 | -60.9803 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b832c73-c00b-3af4-8005-51ac16201c3b | 0.04171 | -60.99477 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98e2ed50-fdec-396d-9cc3-89a254644bd3 | 1.50316 | -59.92015 | 2026-03-05 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e8258e0-a8f1-30d1-8e5e-ff3063a2d8b8 | 2.78118 | -60.3313 | 2026-03-05 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 561a7948-f765-3c2c-8f5b-b36f2c1f071d | 0.05209 | -60.97649 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0e4bd0c-c7eb-3ec8-b00e-5e9c3d9a50ab | 1.00623 | -59.50813 | 2026-03-05 05:54:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87ee91f9-a52f-3b5f-897f-44b142e65e67 | 0.04139 | -60.97614 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d80f5566-44e6-3c4b-9fc6-de720097ade4 | 2.69608 | -60.66076 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49aae852-e76a-386c-adef-1cfc83823451 | 0.04842 | -60.98125 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78a7da65-9454-31d3-a89b-c7767153b2e2 | 1.15772 | -60.88934 | 2026-03-05 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2210d68e-3545-377e-bf83-d6e7e2b47f1e | 2.66267 | -60.40506 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10eb6c88-855d-3e39-932f-bd772abe3222 | 0.37139 | -60.37655 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ec71ced-4012-3c68-86d8-c8f563742653 | 0.04408 | -60.98186 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b89e68ab-ff12-39a3-9ef1-b343112b2fd1 | 0.49712 | -60.50644 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c3e209d-d40c-3ed0-9ddc-2907d42b4b31 | 0.04907 | -60.98538 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4bd2eb79-dceb-3cfe-abdc-4a19019df9e1 | 1.94471 | -60.81773 | 2026-03-05 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README11.md)
