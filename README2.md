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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7ccd7f2-368a-3dd1-b10b-6aa897ffce58 | -12.073 | -52.0197 | 2026-06-28 00:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 131.8 |
| d0c14687-9b1b-30e9-83a0-51c2c37c0aed | -11.5243 | -54.7872 | 2026-06-28 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| c0cacfae-5c10-35e5-ba59-95d971889cb8 | -10.3128 | -57.1367 | 2026-06-28 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 814bf75a-cf6b-361a-bdbc-500fc41524d3 | -12.0923 | -51.9966 | 2026-06-28 00:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 2208bb04-8678-3a5b-90ed-7e5b313d15cb | -12.4654 | -58.481 | 2026-06-28 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| ecba32b5-1013-320a-af37-656d9fea4d64 | -11.209 | -54.3053 | 2026-06-28 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 59511f05-bd52-3d0f-b04f-f8db57af9085 | -12.092 | -52.0176 | 2026-06-28 00:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 317.6 |
| 57477b9f-1181-358c-99e4-165328d39a00 | -12.4651 | -58.5009 | 2026-06-28 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 894a16b4-4ee9-3dd3-9e9f-848e2bc7b087 | -14.0594 | -58.208599 | 2026-06-28 00:33:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 13b65969-96c6-30ba-8605-3c0d13c42de7 | -11.9134 | -57.1301 | 2026-06-28 00:33:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6cd8af2d-d0b6-3e29-9fe3-e379f527c060 | -12.7933 | -54.871201 | 2026-06-28 00:33:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b031f66-739c-3dd2-9891-81bca257b5d9 | -12.1793 | -52.8992 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37d0ec55-b525-34f9-8203-e2a5a0d41b30 | -12.1957 | -52.880501 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27dfb622-dde4-301a-a08a-8fbd296b4056 | -10.5352 | -53.700001 | 2026-06-28 00:33:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| adc8c6fc-4b21-3508-8caa-6f3ee477973f | -12.1844 | -57.1516 | 2026-06-28 00:33:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8383bc4d-0a21-3594-88f8-28b7b12b3660 | -10.3022 | -57.124802 | 2026-06-28 00:33:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b044d1f-747d-3a37-a2bc-ac3ffd835c39 | -9.0936 | -59.3834 | 2026-06-28 00:33:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de6b0d0c-7dc9-3969-b22f-2558b5a4d873 | -14.0573 | -58.198299 | 2026-06-28 00:33:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e689579e-9ced-3330-abda-ad6e15d012ed | -12.1761 | -52.885101 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82e13eb5-a08f-32b7-be71-065ad0433efe | -12.6103 | -57.8657 | 2026-06-28 00:33:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7434b657-d3f2-35ff-ad07-422e0a9395a6 | -12.1655 | -57.111099 | 2026-06-28 00:33:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f9a0adb-5a0f-33d0-b88a-b4be5c8bb2a2 | -10.9394 | -56.842899 | 2026-06-28 00:33:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9cb41110-f807-3270-ad94-d7f0fd350f74 | -12.1825 | -57.143002 | 2026-06-28 00:33:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b247213b-e636-394a-aede-7fde2b8a105b | -12.2007 | -52.856899 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb27c579-8255-3f41-bdfc-63aa1bb0ce9d | -9.098 | -59.403999 | 2026-06-28 00:33:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5fda9a1-a219-3ae4-aedb-0b736d2fe6eb | -11.9259 | -58.656799 | 2026-06-28 00:33:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6ad2f962-5382-3568-aa81-e918edc43fb3 | -12.2281 | -56.536598 | 2026-06-28 00:33:00 | METOP-B | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db96c1b1-7583-334f-8a97-48f9b7c3e97d | -12.1003 | -52.011101 | 2026-06-28 00:33:00 | METOP-B | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 370b1b94-fc7f-3913-9e85-d1aa1c11744d | -11.9098 | -57.113201 | 2026-06-28 00:33:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae5ef535-c2f1-3e72-9006-f5e42a128adb | -12.1789 | -57.125999 | 2026-06-28 00:33:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09c44989-47fb-36c2-a5a0-f61a3a6db362 | -12.5985 | -57.858398 | 2026-06-28 00:33:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46d67f64-0268-385a-b203-06d4fde100e4 | -18.480499 | -54.085098 | 2026-06-28 00:33:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d0fc3f19-fd8c-3545-b488-af2d6b83141e | -12.4494 | -58.472 | 2026-06-28 00:33:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2904617d-fb81-3ab4-b3f7-ba66db8d6712 | -12.1973 | -52.8876 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5780ce3b-55fa-3377-8166-e6987b7bd831 | -12.5472 | -57.1721 | 2026-06-28 00:33:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c68fd58-5146-320e-ac1c-92901715d6f0 | -12.0773 | -52.0009 | 2026-06-28 00:33:00 | METOP-B | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df6832c2-1422-3fb5-829e-0c89bea48580 | -12.2379 | -56.534401 | 2026-06-28 00:33:00 | METOP-B | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8014705-faa5-3715-958e-4e9a6752ac3b | -12.4634 | -58.490299 | 2026-06-28 00:33:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0957a414-ccfd-3d5c-a44a-6f132b960a77 | -16.0403 | -50.557999 | 2026-06-28 00:33:00 | METOP-B | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2b21bc25-7c38-3444-9e6a-958014971c71 | -12.6122 | -57.875198 | 2026-06-28 00:33:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3c9da01b-f26c-3a0f-9f5f-c51f6a269fcd | -12.6239 | -57.882599 | 2026-06-28 00:33:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9cbfd834-c03c-315d-9fb5-d1a281c749df | -12.1925 | -52.866299 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b95bfeea-7ce3-385e-8920-39d8868594af | -11.5275 | -54.775902 | 2026-06-28 00:33:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe5dd829-3ab9-3f7b-80c0-5ceb72c5e03c | -11.6712 | -57.244598 | 2026-06-28 00:33:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98398266-5732-3a45-aee3-980f3a30aed3 | -10.312 | -57.122601 | 2026-06-28 00:33:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb2a7fe0-d2d9-315b-9f32-2cedbef7bd79 | -12.6024 | -57.8773 | 2026-06-28 00:33:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 135f8729-8d40-3250-b858-faa87322a75c | -12.1709 | -57.1367 | 2026-06-28 00:33:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9005a3e4-b6f8-3095-8211-040ac0a570e2 | -12.079 | -52.008301 | 2026-06-28 00:33:00 | METOP-B | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43e8bf85-8298-316a-851b-0e25866f102e | -12.4348 | -58.401199 | 2026-06-28 00:33:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| af715f61-895d-3f9b-bb3a-afdde073295b | -9.1882 | -58.0499 | 2026-06-28 00:33:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 665d6fc2-2b9f-3cfd-9b4e-c99ce8b8c778 | -12.1989 | -52.8946 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa45597c-9aa0-3387-842c-a233c473bc01 | -14.0475 | -58.200298 | 2026-06-28 00:33:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d66af46d-f36e-3bb7-8714-84325c441cef | -4.2774 | -48.361599 | 2026-06-28 00:33:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 067cb7ac-69d8-32a0-b50d-be33b4506cb4 | -12.4613 | -58.480099 | 2026-06-28 00:33:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 226dd7a1-7c03-3c49-9661-e11f630d4c9d | -4.2739 | -48.346802 | 2026-06-28 00:33:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71ca908a-8b9c-3f3f-9e25-1a3b46646d05 | -12.1691 | -57.128101 | 2026-06-28 00:33:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89274cc3-5dcc-34db-bb53-494cfea61715 | -18.4837 | -54.1003 | 2026-06-28 00:33:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b9d4a9ea-82b7-37bf-811d-2b7d6f103889 | -10.3005 | -57.116699 | 2026-06-28 00:33:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9f84fd7-7828-330d-ac9c-3a8e6aaa4c8d | -9.0958 | -59.3937 | 2026-06-28 00:33:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4e3697b-6e06-3a7f-8b27-e143a725d905 | -10.779 | -54.0965 | 2026-06-28 00:33:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 070653fa-0549-390a-90ce-4cfe07f1431e | -9.19 | -58.058601 | 2026-06-28 00:33:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50dcacf5-874e-3ab3-bb92-db41a3078032 | -13.2543 | -54.392601 | 2026-06-28 00:33:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a316654-1a5a-32e8-803b-c693dad33003 | -12.0551 | -55.446999 | 2026-06-28 00:33:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06edf8ac-4e11-359a-8ddd-84345e7d133a | -11.9116 | -57.1217 | 2026-06-28 00:33:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e061d0a9-97a4-3e08-b041-a0e34f485e90 | -10.3039 | -57.1329 | 2026-06-28 00:33:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8c5b316-6e40-3028-a274-e147d0ad52ef | -11.8866 | -57.100601 | 2026-06-28 00:33:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ba6a96b-5c40-3f11-89ea-ef78f2015c5e | -12.0854 | -51.9911 | 2026-06-28 00:33:00 | METOP-B | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ade88f5-1713-350e-ba08-6aaedf23cdb0 | -12.2298 | -56.544601 | 2026-06-28 00:33:00 | METOP-B | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c2951dd-74ee-344a-8958-5937f64357da | -10.9411 | -56.850899 | 2026-06-28 00:33:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31feb751-6afc-3130-9fe8-3a5a772ed6c9 | -12.2413 | -56.5504 | 2026-06-28 00:33:00 | METOP-B | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d966ea30-1d73-3a60-ada3-eaffbc02c469 | -11.5306 | -54.790001 | 2026-06-28 00:33:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dcca33e3-c8aa-3a5f-b017-3934a0b4b2fd | -9.5976 | -56.9044 | 2026-06-28 00:33:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3aa6b50e-5517-39ab-9ecf-295703dd1515 | -11.9238 | -58.6465 | 2026-06-28 00:33:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6eabc238-f4de-3364-99e2-f69c713fb262 | -14.6343 | -54.4478 | 2026-06-28 00:33:00 | METOP-B | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aa100a9e-41e8-398d-9d01-0cc532e40e05 | -11.9062 | -57.096401 | 2026-06-28 00:33:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a73d05df-722e-3e3b-8f74-d3132e67e852 | -12.1859 | -52.882801 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dfe6746c-8315-3c7f-8c6d-22a8ab955fc4 | -12.0905 | -52.013401 | 2026-06-28 00:33:00 | METOP-B | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e24000b-b85d-3fc5-bab6-f50b320d1fbf | -11.2107 | -53.815498 | 2026-06-28 00:33:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d4d542b2-c8f4-32da-95e5-a27a48e89432 | -12.0888 | -52.006001 | 2026-06-28 00:33:00 | METOP-B | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02b956a4-c435-3dd5-bba6-a7ccf29ebd99 | -9.0838 | -59.385502 | 2026-06-28 00:33:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0702a3c8-f3c1-3520-98a8-159f17c48a3e | -14.0496 | -58.210701 | 2026-06-28 00:33:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2372fa60-476b-3141-b66f-20898653e88f | -11.9188 | -57.3983 | 2026-06-28 00:33:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8a90670-8ed8-34e5-a475-4cf7148aa0f7 | -10.6363 | -50.517601 | 2026-06-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66afcbff-ebab-3338-9bea-a98b4b404f24 | -12.2396 | -56.5424 | 2026-06-28 00:33:00 | METOP-B | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a647c24-f162-3515-a12f-8f4c101a5a74 | -11.6596 | -57.238201 | 2026-06-28 00:33:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 638804ab-beef-3cc9-86a6-75c92e3253bc | -11.324 | -54.461498 | 2026-06-28 00:33:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f96d7640-4aef-3eef-bc8b-52ad6d06136d | -12.1923 | -57.1409 | 2026-06-28 00:33:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52e03518-6907-37f1-8873-fa0e04cd9367 | -11.2205 | -53.813301 | 2026-06-28 00:33:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e0bc8d7-027e-39ad-91c1-9068c5e1681c | -12.2713 | -50.091702 | 2026-06-28 00:33:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c15ed484-79e1-39b8-bfad-85d1982f5622 | -14.6359 | -54.455002 | 2026-06-28 00:33:00 | METOP-B | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9b54d0a1-7879-3a61-8662-30608bd7d4d5 | -12.1875 | -52.8899 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50e4c4b9-f8fe-3b7d-b55f-4b2e474dc257 | -10.9376 | -56.8349 | 2026-06-28 00:33:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a38468b6-f947-3091-86ca-211f3cf0d1c0 | -17.297001 | -42.620899 | 2026-06-28 00:33:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8a6b88b4-4e10-3ced-bb82-b883d4b22794 | -12.0986 | -52.0037 | 2026-06-28 00:33:00 | METOP-B | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8340be9-77e2-3ab3-9b3c-b4793549ca18 | -11.673 | -57.253101 | 2026-06-28 00:33:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53cab782-56b3-3b3d-bd22-d63031669519 | -12.2734 | -50.100498 | 2026-06-28 00:33:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0318b9bb-8595-3a68-ae55-363f66a43aad | -10.578 | -50.140999 | 2026-06-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fd776b6-e99b-39e3-a7c5-af3641370778 | -12.4592 | -58.469898 | 2026-06-28 00:33:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bbc730cc-ab3a-368c-b843-efdc6c0ee2ef | -12.6005 | -57.867802 | 2026-06-28 00:33:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 47310482-cf94-3bc1-8e3b-00caa0b7bc15 | -12.0807 | -52.015701 | 2026-06-28 00:33:00 | METOP-B | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
