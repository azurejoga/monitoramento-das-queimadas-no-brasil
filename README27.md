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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d20c0f23-7e5f-3989-9ba7-e64101ef9822 | -13.71622 | -48.80898 | 2026-09-26 05:14:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 816b8233-f5be-3f3d-aba7-69451748e4a2 | -16.76423 | -47.25227 | 2026-09-26 05:14:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18d6a13e-8202-3172-9714-92ea67e940a7 | -14.47596 | -53.6357 | 2026-09-26 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1f061e34-2313-3843-9812-21d1b8c02522 | -26.42118 | -52.35106 | 2026-09-26 05:16:00 | NOAA-21 | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ad607ae3-0681-3d57-beb5-f252d5aa0bcc | -22.02181 | -49.57816 | 2026-09-26 05:16:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 04cdbd0c-658b-3342-8922-8dd81ef5ff6c | -22.02225 | -49.57325 | 2026-09-26 05:16:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 21b5e159-569a-3385-be14-c1f80473dee2 | -23.00241 | -48.6246 | 2026-09-26 05:16:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a5a2cdc-f979-370f-9237-111e7bddecd5 | -21.53843 | -50.2474 | 2026-09-26 05:16:00 | NOAA-21 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| de716785-f5e2-3d5c-a457-e17aa4598f54 | -20.09706 | -57.21142 | 2026-09-26 05:16:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2c55723-ca88-34f1-84db-4ea83cde809a | -21.53966 | -50.24817 | 2026-09-26 05:16:00 | NOAA-21 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c6d47f8b-d9d0-3190-ac32-8b66ffdcbdda | -21.96814 | -55.93708 | 2026-09-26 05:16:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4758eb32-2e82-3d8d-9d48-29530a3b2cfc | -23.00282 | -48.61902 | 2026-09-26 05:16:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6f6ec2b-949d-3dd9-9176-9c5170542e2a | -21.96367 | -55.94016 | 2026-09-26 05:16:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 612e4b82-18e2-36be-bf01-c991268c1858 | -26.42086 | -52.35476 | 2026-09-26 05:16:00 | NOAA-21 | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 19772452-52b9-3399-8693-a4843cee302f | -21.54417 | -50.24812 | 2026-09-26 05:16:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c1bcdb39-3b54-337f-92f3-ace4ff6e554d | -21.91494 | -56.92862 | 2026-09-26 05:16:00 | NOAA-21 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5e2934d-61bb-31d7-96ef-bf50ee2352af | -29.12689 | -55.62196 | 2026-09-26 05:18:00 | NOAA-21 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 0d7ee0bd-35d2-31e8-b126-9e83c53bdb11 | -28.67497 | -53.60171 | 2026-09-26 05:18:00 | NOAA-21 | CRUZ ALTA | RIO GRANDE DO SUL | Brasil | 4306106 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cec6c69b-ca36-3368-9e94-b67e9a7de444 | -2.90531 | -54.09882 | 2026-09-26 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 000b3e40-3fcf-3336-9c17-aa5078e87711 | -3.00189 | -50.47023 | 2026-09-26 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| babbdc89-5e50-35f0-9b8f-a6a81670e480 | 2.88216 | -60.29474 | 2026-09-26 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82b9ba77-d7d9-3519-93d6-d793f8504bd7 | -3.20321 | -53.41107 | 2026-09-26 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da08702b-1532-32a1-a9ab-09555553f04e | -1.69036 | -55.56149 | 2026-09-26 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ecf66d41-b126-397d-8411-ca04d4643133 | -2.06928 | -56.86292 | 2026-09-26 05:46:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd55045e-46c8-3992-99d0-8184f9df7bb4 | -2.5741 | -54.74882 | 2026-09-26 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4836cde6-4f7c-3410-a0a3-4638b3371d51 | -3.83899 | -55.90583 | 2026-09-26 05:46:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a5b4d10-2c91-37d9-8e90-1a3e723a79b5 | -3.22384 | -54.3252 | 2026-09-26 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93fd96c4-5435-3306-8f1f-42a7de8c309a | -1.14431 | -54.09883 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f990fe8-2c7e-3fad-8320-fe4c9c13bd6e | -3.22812 | -54.33207 | 2026-09-26 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 858777c2-0226-3e4c-a755-bf3051e3d9a8 | -3.42136 | -50.42445 | 2026-09-26 05:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24864058-a9d0-3809-9f4b-5270d7be7c82 | 2.9391 | -61.26856 | 2026-09-26 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fdae4aad-602e-3577-b92e-bc7e023769fe | -1.31592 | -54.57155 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f31ff96-29b3-33dc-bf15-5025f0235a8e | -1.26723 | -55.84253 | 2026-09-26 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4dafeab0-6cf8-3f97-843e-984efc214c08 | -1.14942 | -54.09962 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| faced86e-22ce-3456-b2a4-8001fb102640 | -3.71562 | -54.64917 | 2026-09-26 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 410431ed-2a83-34b6-8cd8-afd6aae0b4e3 | -1.21983 | -54.56062 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 787d064e-eda9-3974-a1c0-0cb5b6e453d7 | -2.90069 | -54.09475 | 2026-09-26 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1f4a137-5000-3029-b1c4-c3e4e7c83e24 | -1.8438 | -54.71758 | 2026-09-26 05:46:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f7541aa0-28ce-32e2-b8a8-e7f96720ebbf | 2.90012 | -60.27726 | 2026-09-26 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e4e79cce-87f5-3fa5-a307-f020f5f13a98 | -3.26904 | -50.14691 | 2026-09-26 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c4219446-36ec-3cbc-ad3a-55ab12a308c1 | -2.94949 | -57.71812 | 2026-09-26 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f7f94db-1f69-38e4-9924-24876c219572 | -3.2039 | -53.40839 | 2026-09-26 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5b621a3-8667-378d-8286-0c61feddf0d8 | 1.56979 | -56.05592 | 2026-09-26 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff3a2fb5-d9c8-31f1-96be-eacf6d72e26a | -3.22904 | -54.32597 | 2026-09-26 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0588e679-03c3-36ec-b2a4-fa9f238c05d2 | -1.14478 | -54.09584 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8648e751-944e-30b0-82ef-9363da91d011 | -1.29764 | -54.22237 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c6b1dfb-008b-3795-9d68-8fe0dd0dd493 | -1.30277 | -54.22284 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ae56e34-3979-3664-b522-923a24960367 | -1.14384 | -54.10184 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cda40fca-8c5c-325b-98de-49628cb5979d | -2.57403 | -54.74808 | 2026-09-26 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f44c3f75-1bfd-3ddd-9000-d571423c9d4c | -3.83826 | -55.91074 | 2026-09-26 05:46:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4a88578e-a616-338f-8674-e2e9fecf5c3b | -3.30248 | -54.68958 | 2026-09-26 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c12f62e-f4c3-3ccb-a921-4dadc64d3762 | -2.1518 | -53.71264 | 2026-09-26 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af7f082b-d955-3d4d-a31e-113c6f6937a0 | 2.94188 | -61.26458 | 2026-09-26 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72d47d4e-e9b8-324e-9193-f531483e4a60 | 2.53649 | -60.36005 | 2026-09-26 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af8623af-93b5-39b6-a79c-3297a1b12edd | -3.50013 | -53.45633 | 2026-09-26 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d45129dc-7fdc-36b8-b50d-aa7f7319fdc4 | -2.73354 | -54.90606 | 2026-09-26 05:46:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84e8ac7a-cd55-362d-a49d-aa7386b87c05 | 1.29554 | -50.83351 | 2026-09-26 05:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d54a0bea-8ea0-3a6c-8240-daf28469768d | -3.71518 | -54.65214 | 2026-09-26 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 983197e9-4c44-3df4-bf25-9f7432b40f30 | -1.15084 | -54.09063 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6d7df94-0b62-3dca-8c90-e95374e0bf0d | -1.21391 | -54.56587 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f9de445-5786-3153-9c40-13d2e7211205 | 1.01156 | -60.10795 | 2026-09-26 05:46:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49237e00-c810-3907-b151-3635dd600626 | -3.69319 | -54.26026 | 2026-09-26 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8441cc3b-3d51-3b79-938e-671f5d7af9a3 | -2.90006 | -54.09805 | 2026-09-26 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a1a6e43-bdfe-32c0-9ff0-afba0faadc96 | 2.62238 | -50.88939 | 2026-09-26 05:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0d652b4-2444-33db-bbe1-34a91e73a693 | -3.22858 | -54.32903 | 2026-09-26 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e07866c-316b-38ce-99d1-b18459acd8c6 | -2.97455 | -51.04821 | 2026-09-26 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb65e411-c1b5-380f-89c0-a092fce0753f | -1.21417 | -54.56681 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7e6c771-f6c5-36b4-a280-3eee6f5bca98 | -3.26499 | -50.13976 | 2026-09-26 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd623806-bdac-3b7e-b7a9-93ef08663167 | -3.6875 | -54.26237 | 2026-09-26 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcf36c52-37f1-3c4a-b5b0-bcdc30f747ce | -2.99441 | -50.47474 | 2026-09-26 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6f4e8d8-b420-340e-adb0-c3de41d7c9d2 | -2.15844 | -51.97845 | 2026-09-26 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a046edc-5e59-3a71-9cfd-e6fcf94eb42d | -1.15036 | -54.09362 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3809b0ab-7821-30ba-a875-cd15f6f50dcb | -2.15551 | -51.97531 | 2026-09-26 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23fd823e-f67f-39d9-a5ed-fae0de17653f | -1.83884 | -54.71689 | 2026-09-26 05:46:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4610e450-10f5-3994-9d6f-3f80c0db561e | -1.98291 | -56.69287 | 2026-09-26 05:46:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54a66139-87fe-31b2-b46e-fa202b0074d7 | -1.21912 | -54.56761 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75263333-4df3-3e9c-8bca-a3d97ccf1140 | -1.34298 | -55.47622 | 2026-09-26 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a037a66-5cd3-38e8-a5a9-a9f062477b57 | -2.91343 | -54.11642 | 2026-09-26 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 820e598e-92c8-3435-9f27-e833db0b397d | -1.83907 | -54.71765 | 2026-09-26 05:46:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 5d47f049-57ca-3bcc-ba88-15444ef11611 | -2.90819 | -54.11562 | 2026-09-26 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34a43f97-3dbe-3f27-834e-397b27391d1b | -3.20942 | -53.40923 | 2026-09-26 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45cbedeb-2cab-3502-a730-362bd006a359 | 1.58575 | -55.81703 | 2026-09-26 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5426923-c279-3fbc-8957-dffa2662a0e3 | -3.23377 | -54.32983 | 2026-09-26 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8ae2b52-4a9b-3b26-b8c8-5b285b6f59be | -2.06866 | -56.86692 | 2026-09-26 05:46:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cfeac5d5-c6c6-3210-98d3-f5933a6f72c6 | -2.90867 | -54.11241 | 2026-09-26 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7606041e-3f47-3edd-a32a-b7a29c06a1ab | 2.88159 | -60.29116 | 2026-09-26 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74252855-41ee-3dd5-827d-b93d2d9f5f8f | 2.71741 | -60.68353 | 2026-09-26 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9523a0ea-dabc-3006-a285-cc3387e87903 | 1.62648 | -56.03872 | 2026-09-26 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 11ab3f7a-de5b-3a0a-b0ac-d88809997058 | -1.11314 | -57.05506 | 2026-09-26 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61c618dc-7e57-3f83-9f97-70ac3f7621a6 | 2.93855 | -61.2651 | 2026-09-26 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 603ceb01-7250-3511-a734-a719d503c9d7 | -3.2295 | -54.32291 | 2026-09-26 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0c5f039-3f6e-3040-8532-29da9e41ef40 | -1.69214 | -55.56343 | 2026-09-26 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f9ac9fd6-a8d0-35e7-b97d-bd87a91901d0 | -3.72118 | -54.64702 | 2026-09-26 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 398efc3c-3885-3dfb-9d14-dbb037bb0e14 | 1.01215 | -60.11166 | 2026-09-26 05:46:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ec57613-b185-39eb-ab74-cdbc82505120 | -3.26413 | -50.14571 | 2026-09-26 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72f68a76-cd0d-34b4-a47c-91ff32572ed2 | 2.65626 | -61.31692 | 2026-09-26 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ca00015-518a-3dfe-9a35-1a8792487837 | 1.58642 | -55.82112 | 2026-09-26 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ef774c15-39ee-3c33-a3af-64dea6350987 | 2.88273 | -60.2983 | 2026-09-26 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59366363-7f77-3103-af1d-24aff1ef1f42 | 2.89338 | -60.27833 | 2026-09-26 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94ce8783-4581-32b0-95a2-26d9ea6650e4 | -3.42218 | -50.41867 | 2026-09-26 05:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README28.md)
