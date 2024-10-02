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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fdb73f0-c1e4-3036-b9b7-6d9b30cc1d68 | -21.3661 | -55.6807 | 2024-10-02 02:07:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 100.0 |
| eded84c3-d225-36e3-a4b4-5c28e8b9a5d6 | -22.3713 | -49.3011 | 2024-10-02 02:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.8 |
| 7ffd5049-b47a-370e-84b3-3a071bb3cc02 | -22.372 | -49.2777 | 2024-10-02 02:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 130.7 |
| 838bf383-9d3b-3e3d-9cb0-1d01ff86a3e3 | -22.3922 | -49.2961 | 2024-10-02 02:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.2 |
| f8b0a44e-873d-3e4a-ad6b-1ae86be9d3ed | -22.3929 | -49.2727 | 2024-10-02 02:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.7 |
| 73fd5ac0-d9ed-335e-97e8-1cd670eff5b2 | -22.9277 | -43.7243 | 2024-10-02 02:07:11 | GOES-16 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 58.9 |
| 6390b8d9-fca7-3585-bc4b-5fc7b7f1ffed | -17.838301 | -57.712799 | 2024-10-02 02:09:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ec2f3401-cdef-3ea1-bc98-137f915c9597 | -16.8797 | -57.660599 | 2024-10-02 02:09:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 64f33642-0502-3e76-ace5-1b8fc3ca05b1 | -16.8895 | -57.694199 | 2024-10-02 02:09:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 225261da-79cd-3db6-8528-4d939d09480e | -16.870199 | -57.663601 | 2024-10-02 02:09:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ce046d04-46e9-3aa8-a444-80b046dca5a3 | -16.8801 | -57.697201 | 2024-10-02 02:09:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9ae73644-0b16-3b62-8f94-d973bf1fb33b | -16.683701 | -57.344002 | 2024-10-02 02:09:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a09a8dcf-afa6-3e1a-92d4-ab928740afc1 | -16.5853 | -58.181801 | 2024-10-02 02:09:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1a1e2738-1d66-35ac-bf97-016f3a1bd08f | -16.5944 | -58.213299 | 2024-10-02 02:09:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 617bea1a-a886-3c7a-a1aa-902aec846084 | -16.603399 | -58.244701 | 2024-10-02 02:09:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e393a8eb-2f5c-377d-b3e9-1024d506d706 | -16.5758 | -58.184799 | 2024-10-02 02:09:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 96c2c3a6-5879-3f06-b189-da1ae7709591 | -16.5849 | -58.216301 | 2024-10-02 02:09:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 03bdaed7-db71-37cf-a34e-d76d2bd6fa34 | -16.593901 | -58.2477 | 2024-10-02 02:09:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ae6a1d1e-a56a-3535-a6f3-4d2e40072636 | -16.566299 | -58.187698 | 2024-10-02 02:09:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 92eef7ec-b877-34cd-ab7f-8293f812b5de | -16.5844 | -58.250702 | 2024-10-02 02:09:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 48e44b1e-e854-3da5-84a2-8b3e9d78a8a0 | -16.566 | -58.222301 | 2024-10-02 02:09:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b8708054-b833-302a-99a8-640d7ede60ce | -16.575001 | -58.2537 | 2024-10-02 02:09:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 897044f4-1261-33f0-a32a-a6e90fe77cfc | -12.9589 | -62.657902 | 2024-10-02 02:11:15 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9185d779-6e7c-3101-90a2-6fc970e934b3 | -12.9492 | -62.6605 | 2024-10-02 02:11:15 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e84d616e-8c4a-31f6-a5b4-9070dc66d673 | -12.9541 | -62.6791 | 2024-10-02 02:11:15 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 66f7df97-ca9e-3d42-aad0-97ed80c69337 | -12.9396 | -62.663101 | 2024-10-02 02:11:15 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb7e5fe-1b89-3b9a-a78f-03a4be75170d | -12.9445 | -62.681702 | 2024-10-02 02:11:15 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1d2f4406-1f6e-3523-ad93-7feb20e403ce | -12.9493 | -62.700199 | 2024-10-02 02:11:15 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 730a47e1-0fd1-3f64-8d6b-c013ca8468ce | -12.9348 | -62.684299 | 2024-10-02 02:11:15 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e9f0e4d3-0533-30a4-88de-dd34bcecaf63 | -12.9396 | -62.702801 | 2024-10-02 02:11:15 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 114f0d8e-a5f5-330b-a16d-0d958d72280e | -12.9251 | -62.686901 | 2024-10-02 02:11:15 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a3c26dd9-b5d7-35be-b9c1-5392cc65a084 | -12.9155 | -62.689499 | 2024-10-02 02:11:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e17139ee-55e5-3cb2-ae21-0d2ce1ac792b | -12.8569 | -62.504101 | 2024-10-02 02:11:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 77e1bdb0-2cd6-3883-a9a3-ade07601c82c | -12.8618 | -62.523201 | 2024-10-02 02:11:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c9fd820d-6fd6-3b1e-bea2-e0583ae861e6 | -12.8472 | -62.506699 | 2024-10-02 02:11:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a4ede0f0-daf4-3644-8d72-514ce4772c00 | -12.8522 | -62.525799 | 2024-10-02 02:11:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a2750bf4-bb3c-35ad-b0e2-e6abb8f0494e | -12.8376 | -62.509399 | 2024-10-02 02:11:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e4b9cfcb-c118-3a86-a5dc-35342be00907 | -12.8426 | -62.5285 | 2024-10-02 02:11:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4d12ed18-4e40-39e8-9903-64b3fffde41e | -12.8475 | -62.547501 | 2024-10-02 02:11:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0ecd0158-d286-3a93-a95b-56a6f25c0a33 | -12.8279 | -62.512001 | 2024-10-02 02:11:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fcf9af1c-e74f-3860-96fc-a887f99c951c | -12.8329 | -62.531101 | 2024-10-02 02:11:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e90c29a8-9d86-3f52-8e0a-1e92cf82aa9e | -12.8379 | -62.550098 | 2024-10-02 02:11:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dd8f011d-4a8b-3c1a-bd10-7ddcfd79d84c | -12.8183 | -62.514599 | 2024-10-02 02:11:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d24e47ae-fcfd-3bf9-b922-e30951d5b5ec | -12.8233 | -62.533699 | 2024-10-02 02:11:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a83ec068-dcec-3171-86cd-9481b9f939ff | -12.799 | -62.519901 | 2024-10-02 02:11:17 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cb6a5ee7-1388-30d0-a62c-df547cdd67a9 | -12.804 | -62.539001 | 2024-10-02 02:11:17 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 49b406aa-855f-3d2d-895d-049bd0607963 | -12.8623 | -62.763199 | 2024-10-02 02:11:17 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2f72de13-2dad-34eb-b563-fd27c5c339f8 | -12.8477 | -62.7868 | 2024-10-02 02:11:17 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a04e1999-9451-316d-bd4d-0ad9eae2b83e | -12.6911 | -63.0597 | 2024-10-02 02:11:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 426d7c97-0a9d-346f-9086-50c57a8f6ae3 | -12.6473 | -63.090302 | 2024-10-02 02:11:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 82c4e450-238f-36c5-8e7c-a0713628bb01 | -12.6518 | -63.1078 | 2024-10-02 02:11:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eb8afe80-15e4-3ee1-92ca-a87d298a5411 | -12.6377 | -63.092899 | 2024-10-02 02:11:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 97f0f311-bb69-3c78-bc74-f0a93e801360 | -12.6422 | -63.110401 | 2024-10-02 02:11:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bfa7f61f-8e09-3765-ad01-e628d120d3f2 | -12.6325 | -63.112999 | 2024-10-02 02:11:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e4f39f76-5658-3593-91cd-e6af41d7acbc | -12.637 | -63.130501 | 2024-10-02 02:11:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cda4a419-eb34-3784-a209-cb04b496b05d | -11.6596 | -63.994202 | 2024-10-02 02:11:41 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d60acd64-0607-3597-8dd4-21e5e9ac28f8 | -11.5593 | -63.761501 | 2024-10-02 02:11:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8f708144-6f2d-3263-8f9e-d6205d80b778 | -11.5635 | -63.778 | 2024-10-02 02:11:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8b79616f-2254-312b-b948-5b8709508dbe | -11.6209 | -64.004402 | 2024-10-02 02:11:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4c6f2b70-c14c-31a3-8111-14bda5c9ceab | -11.6249 | -64.020203 | 2024-10-02 02:11:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f6061ba3-022d-3a94-a85e-3c462295814a | -11.5539 | -63.780499 | 2024-10-02 02:11:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a4362467-aae7-3cfe-8fd5-5ba0a61e5566 | -11.5386 | -63.802101 | 2024-10-02 02:11:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1b4e71a6-975d-3618-b750-c4d5f92c2c4d | -11.5428 | -63.818501 | 2024-10-02 02:11:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 913f5a3f-7ea5-3dd1-8a30-e23b289ad0ab | -11.6724 | -64.991798 | 2024-10-02 02:11:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7528209e-baa4-3df6-8398-b6a17d83aef9 | -11.6757 | -65.005402 | 2024-10-02 02:11:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dfc6625e-4830-378a-bdbd-268544ecd4ab | -11.6559 | -64.967003 | 2024-10-02 02:11:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 996d5dd8-4e7d-359e-b7eb-5280ba7a800e | -11.6593 | -64.980598 | 2024-10-02 02:11:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9826baec-8610-34b7-86d2-1f6600471706 | -11.6627 | -64.994301 | 2024-10-02 02:11:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6d707303-3783-3058-b900-edb2ec384b8d | -11.666 | -65.007896 | 2024-10-02 02:11:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c5335048-0909-36d9-b313-e5b0f12f59c1 | -11.6462 | -64.969498 | 2024-10-02 02:11:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 980d8a27-1502-3d68-82d1-fd0e7d69cd3c | -11.6496 | -64.983101 | 2024-10-02 02:11:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ad87da5d-ae88-3122-8e63-fd935175f489 | -11.653 | -64.996803 | 2024-10-02 02:11:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ddcb17b9-b1ce-3ff9-a343-7ea618b82e74 | -11.6563 | -65.010399 | 2024-10-02 02:11:45 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8014882d-8aa3-378e-bb9a-d27792a4fb63 | -11.6433 | -64.999298 | 2024-10-02 02:11:46 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 565eca1d-a12e-348a-845a-bda4fad6d84e | -11.6466 | -65.012901 | 2024-10-02 02:11:46 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b91abcc0-7326-30f2-8ec3-6f2ac3be22bb | -11.6058 | -65.222603 | 2024-10-02 02:11:47 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7e9075dc-6cd1-335e-a65b-9253c82d020a | -10.6258 | -62.811501 | 2024-10-02 02:11:53 | METOP-B | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2b90d509-600d-3da5-962f-761a51027df7 | -9.5403 | -62.7934 | 2024-10-02 02:12:11 | METOP-B | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e3404000-9f31-3aac-b7e2-14d17a572e43 | -9.5456 | -62.814098 | 2024-10-02 02:12:11 | METOP-B | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5580a98a-5d3a-34c9-9b47-90f71ceec95e | -9.5307 | -62.796001 | 2024-10-02 02:12:11 | METOP-B | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 702d8bd9-021c-3673-926d-8c21982fcda8 | -9.9445 | -64.891098 | 2024-10-02 02:12:13 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 00a5a278-01e9-3888-8fc0-4733280c6bb2 | -9.9481 | -64.9058 | 2024-10-02 02:12:13 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a2facbeb-7281-380b-8a20-c83a02f33824 | -9.9311 | -64.878799 | 2024-10-02 02:12:13 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6a934dca-8e25-315d-8d2d-59f3bdf110cd | -9.9348 | -64.8936 | 2024-10-02 02:12:13 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c3267a7c-601f-371d-9d51-5d31976d5bdf | -9.9384 | -64.908203 | 2024-10-02 02:12:13 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1236d48f-f527-35d6-a3af-3628be34fe62 | -9.942 | -64.922897 | 2024-10-02 02:12:13 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bf1e2331-038f-30e6-a6d1-9756a27dd442 | -9.9251 | -64.896103 | 2024-10-02 02:12:13 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0eb4b16f-a3d0-3d46-af26-1ce7f26a130c | -9.9287 | -64.910698 | 2024-10-02 02:12:13 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0d779a66-378c-3809-bcba-a125e502eac1 | -10.8893 | -69.339699 | 2024-10-02 02:12:15 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| fc6fce77-da4e-3837-b1a4-d69a4c15e35c | -10.4634 | -67.748299 | 2024-10-02 02:12:15 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 949a68e9-6ee6-3e81-a5c4-11fbe3b94b0d | -10.8615 | -69.4869 | 2024-10-02 02:12:16 | METOP-B | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0e2c556e-40f3-3d32-b48e-02be38054422 | -10.8633 | -69.494698 | 2024-10-02 02:12:16 | METOP-B | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 28d75b43-8a86-3e37-962a-7b3a90aff394 | -10.4439 | -67.883202 | 2024-10-02 02:12:16 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 008e5fd0-23e5-3ddb-b959-fd867d0f7214 | -10.4461 | -67.892502 | 2024-10-02 02:12:16 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ddce42c9-14d6-3659-843f-4836de7f8d79 | -10.8205 | -69.488403 | 2024-10-02 02:12:16 | METOP-B | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| f37a172d-4d9e-3614-bfe2-92589379e5d3 | -10.3297 | -67.750397 | 2024-10-02 02:12:18 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 43641ad4-9283-30a4-aff9-4e77fc9c2050 | -10.3199 | -67.7528 | 2024-10-02 02:12:18 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 50e718a6-222f-3404-bd8e-96f74f4edf97 | -10.7016 | -69.3759 | 2024-10-02 02:12:18 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 2adbe81c-f336-372e-ae66-6028ae4e2c38 | -10.7034 | -69.383797 | 2024-10-02 02:12:18 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 65466173-3861-3c44-9a03-60aa9136ee5a | -10.7089 | -69.407402 | 2024-10-02 02:12:18 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README43.md)
