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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d46caae-cbac-3830-a594-9111dfecf89e | -9.20647 | -59.47306 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d29eb343-74f9-3efd-b8de-8641e6fca000 | -9.19402 | -59.59689 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c1488c6-b7c2-3e66-8429-7d4534820e8c | -10.45778 | -59.13348 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf168317-fd77-38d3-b4e1-76a794dbbd32 | -9.50948 | -60.52198 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 218dc9a5-c082-3978-a1fc-5f575dd1bbf0 | -5.61464 | -60.23122 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5013cda-8d5c-3d31-85f3-aa3eb6548877 | -5.87622 | -57.7661 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c1a4f811-377c-35a9-83bf-3a01b4257ec5 | -9.95072 | -60.17884 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 14aef3f3-85fe-3647-924a-98a50abdcd8c | -9.16424 | -59.68256 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ea47c0e-d64d-30a1-b0de-ca4e85188cfc | -7.73266 | -67.06856 | 2025-08-23 05:42:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a7d74af-0a18-39db-b6b7-135542089555 | -8.60766 | -62.63548 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fec239d6-bb53-3dfb-ab1e-1ff2a77429bd | -9.52185 | -60.55485 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02c86503-bbf8-38a2-aae4-b6fd732a074a | -9.50585 | -60.51759 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 952565c1-5efa-3a52-849a-874632bd1193 | -5.74924 | -57.59885 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 07f20988-6502-3238-bd0d-a1d9ce7e087b | -9.23975 | -60.47321 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72d52ed6-d3b3-3475-b23c-1ff058529664 | -6.31152 | -59.88409 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e080bdb2-2674-3d0e-bbb3-1229d665c96f | -8.61618 | -62.62814 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be3cce49-e276-382d-a222-9ae8c9a9e62b | -9.22515 | -59.75916 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6ba4360-b50c-38ca-80b0-814aa1e1eb39 | -7.43578 | -60.62847 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8dd4be16-048e-3af8-a5aa-af86760151fe | -14.67327 | -56.61685 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f4217896-feba-354c-93b0-ede0b22a5144 | -14.76342 | -55.99166 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90e6c023-778e-3f13-82a9-a682341f68d2 | -14.25358 | -58.54257 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3980bef-1eed-3f01-97f0-74f4547e6c78 | -13.0322 | -56.87785 | 2025-08-23 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40094620-444f-3ae4-abbf-77c95084eb6f | -14.66556 | -54.92351 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 865e4ae0-56bf-3f5a-a694-452fe6868f3c | -15.02371 | -54.89501 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3b6e07f7-8b5a-300a-a1f1-f46689d4bc21 | -14.67354 | -56.6185 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49fa4eac-fb43-3f3c-abba-aa6cd5539f3c | -14.25941 | -58.53706 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01387d0f-fc7f-3d94-b5cd-eb8539db5e39 | -14.66613 | -54.91798 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b177b5e-978c-39a8-8e1e-d1c39d753a10 | -14.33186 | -58.58036 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5fbb391-8bbc-36b0-b501-da68c3078e7b | -14.77571 | -59.65441 | 2025-08-23 05:44:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f51605c-6bfc-3e3c-8ebc-7dcae1a5c558 | -14.99978 | -54.87157 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7df7ca29-418f-3c32-becf-a08095866425 | -14.67943 | -56.61444 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd7e2f62-0ce8-3bff-8605-6cb4942b62d5 | -14.66669 | -54.91252 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f0eb59a4-2b3c-3c8b-870d-5dfa88ff0404 | -14.75683 | -55.99554 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97dc57f5-d201-3985-9a9e-3341b7d26bef | -13.02659 | -56.8771 | 2025-08-23 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 913c8405-dda1-30ba-a1dd-619f6040405b | -14.66472 | -54.86767 | 2025-08-23 05:44:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c1f301bc-9ced-3cad-8e69-9f63aad7c8bd | -14.31413 | -58.55615 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff679fb7-8f72-3864-986d-282c6925f43d | -14.29198 | -58.52504 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6019cec-56a6-338e-8544-a96c32c0781d | -14.67083 | -56.59064 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ea10f7f-f690-3d58-bcf0-62837308b083 | -14.67397 | -56.61474 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53e7ade8-201a-32cd-9540-75c9c8f0e3ca | -14.29371 | -58.55363 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dfb1b650-2517-3ac4-85fe-085c32f00519 | -14.65928 | -56.58827 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7010ae32-e4b6-3b61-8e91-ed1a5369e9a9 | -14.81228 | -59.63326 | 2025-08-23 05:44:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8f493c2-3c18-358d-a264-6997b09d3d84 | -13.68674 | -57.75867 | 2025-08-23 05:44:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54eaee6a-6df5-30e6-9b43-14a3b9ff6594 | -14.278 | -58.55503 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9cc181c-97a4-31df-a016-f17d3030b410 | -15.05109 | -56.39169 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51d308dc-fe7f-370f-88f0-18e793e3ee32 | -13.69031 | -57.75726 | 2025-08-23 05:44:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b748cd3-3358-39e6-ba35-2a722c809773 | -14.86906 | -59.60728 | 2025-08-23 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b794c00e-0348-304b-b883-fea21afbb92b | -15.06251 | -56.39724 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcb3f934-4819-3641-92f3-ccc71edbca46 | -13.36522 | -54.40707 | 2025-08-23 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcafd5b9-082b-3d28-824f-d4af82be6eb6 | -14.8587 | -59.61311 | 2025-08-23 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ba826034-e2da-36fc-ac3e-cadd19318f60 | -14.86359 | -59.61197 | 2025-08-23 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43b82ced-bf95-31d8-9277-9ab6010597e8 | -14.30903 | -58.55554 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22da77d8-251d-3916-8572-ff7fdc296d65 | -15.05704 | -56.39229 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 952ccac1-9271-39e8-9032-1fe6f6908fdd | -14.66499 | -56.584 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9a9a146-f3f5-3006-a7dd-de2d7b2cc3a0 | -14.67147 | -54.92965 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a287614e-5e65-324e-b6c2-06ea568e81ac | -14.75823 | -55.99308 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0016ee1-3acb-3562-9138-e3ef8b07c2b6 | -14.471 | -55.94572 | 2025-08-23 05:44:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a0740dd-b164-35b6-a552-651ee4d4c97b | -14.6129 | -54.86093 | 2025-08-23 05:44:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5f805dc-a112-3488-a5d0-ac3db8468c12 | -14.27038 | -58.53207 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e089e1f8-1159-3608-aed8-c6e36369ce2f | -14.28099 | -58.53011 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e91a1d1-2c58-3b3f-949b-0ca27a48e82d | -14.66417 | -56.59169 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ade7f980-92cf-3306-bbf8-6d4f5fefb383 | -15.03648 | -54.89878 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e9350a5-732f-30ac-ab39-15abc629d615 | -15.58212 | -54.29314 | 2025-08-23 05:44:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3db2f29-5d36-3d13-94f5-d3d53168b46a | -14.33581 | -58.59024 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 973f537c-64ea-36f9-8291-5f70a36b294a | -14.7197 | -55.38339 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 952f5746-dbc6-3b37-9b51-b17740653213 | -14.66589 | -54.91696 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9f1957c0-545b-353e-80c9-cbe31345f15f | -15.55021 | -55.01596 | 2025-08-23 05:44:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d70b408-0574-31fc-8c1c-dce54504dc12 | -13.37178 | -54.40802 | 2025-08-23 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c09c9c1-37af-3135-bbd1-be96d4e8c48d | -15.54314 | -55.02081 | 2025-08-23 05:44:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ad0a454-ab0c-31bf-9c68-369d831f15c1 | -13.02607 | -56.83421 | 2025-08-23 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67fd1883-f841-3831-af23-5bdce54a2e1a | -14.72363 | -55.38116 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 023ca005-3f5d-329a-8be4-2b6357a7e274 | -15.03372 | -56.38548 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df188d3a-d22d-3f93-a899-a2c668cee1e2 | -14.66467 | -54.92803 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 75d604f2-cba2-3a7e-b0d0-589c64df7563 | -14.67973 | -56.61594 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| baa37ec1-2ba4-3e0d-906a-2cbd0191f456 | -14.75926 | -55.40564 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b351195-1b74-32c8-b1c8-2bc44cfc3bf7 | -14.86886 | -59.60949 | 2025-08-23 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9dbfb2f-c317-3ffb-ae63-580886905596 | -14.66502 | -56.58973 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a129c21b-3030-351e-8667-75b747d40bce | -13.42808 | -57.16933 | 2025-08-23 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be4187ee-e59d-3bf9-9548-e7920fb8d02b | -14.33735 | -58.57787 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3453db42-b9ed-3b49-bd03-24e86cb785ad | -14.75078 | -55.99477 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cfc89bf-efe3-358a-b0de-60c54e7397b1 | -12.58248 | -60.35214 | 2025-08-23 05:44:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03618c3a-c39d-31fa-be1b-f669f0cca535 | -15.0363 | -56.38255 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3aa4fd2e-4a2c-356c-8d8e-fc7b7b86a989 | -14.726 | -55.38404 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f5881e0-796d-3b8a-a566-7d2edeef6969 | -14.67178 | -54.92297 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7a7ff5f-bcc8-388e-8e43-af7565282684 | -14.75872 | -55.98846 | 2025-08-23 05:44:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1d41b3b-9acd-330e-91fb-91852ac32a40 | -14.76966 | -59.66423 | 2025-08-23 05:44:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99eec0ff-a3c3-34b9-a7fd-35682ba6aa26 | -15.03007 | -54.89717 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 51d11566-a9d9-3f86-8487-967e08d31560 | -13.03217 | -56.83094 | 2025-08-23 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4416ba01-d04e-3a67-91a8-a7c53b3f220e | -14.61796 | -54.81306 | 2025-08-23 05:44:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7997bfba-4da1-3fcb-92ab-b6cb2cfae78a | -14.67985 | -56.61057 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1d4ecc06-0f06-3ca6-b040-05695bf22195 | -14.28822 | -58.55615 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 53d40cb8-7144-338a-b892-1f2ed1f178d9 | -14.78661 | -59.64462 | 2025-08-23 05:44:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ada5ea8-df36-381a-98ef-a366a5fd6e72 | -14.67116 | -54.92857 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7bbb640-c325-3710-913e-6a63993f7c26 | -14.2755 | -58.53267 | 2025-08-23 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2917f0c7-8690-3b88-a417-bc546288f363 | -15.01737 | -54.89273 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5835810b-9273-3edd-8fdf-9b2a23b16bbd | -15.02434 | -54.88897 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| be3434c8-bbe0-3fbc-a038-28c1875cf433 | -13.02653 | -56.83034 | 2025-08-23 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3796d3f6-a21b-3e5f-9efb-63771cd7d0d4 | -14.65887 | -56.59183 | 2025-08-23 05:44:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32e2eb76-d591-3917-b7af-ea4aaa320fbd | -13.02748 | -56.82244 | 2025-08-23 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c2f94809-e751-3d81-a606-0dc7c19375f8 | -15.03072 | -54.89084 | 2025-08-23 05:44:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README81.md)
