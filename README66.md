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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 780491e6-481c-3e87-be78-a260cb41b1ca | -15.61237 | -57.46767 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6251e86-4d97-310d-8ba3-0c2e3f2629e1 | -15.61193 | -57.47186 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0a82f657-da1c-3f77-a326-d5683e397d2b | -15.60726 | -57.46359 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f06ef138-f339-3961-98ac-b11e0d9ccb8a | -15.60215 | -57.45914 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2091835-046b-3cf8-a1a3-f7e2c445303d | -15.60088 | -57.47036 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d425bf7-d5eb-34d3-a558-7ce00b187d4d | -15.59702 | -57.50451 | 2024-09-29 05:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59f92b92-749e-39f2-9505-04cb62178fe4 | -15.5966 | -57.5082 | 2024-09-29 05:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ea2b75f-58db-30a6-a057-103689723a00 | -15.59578 | -57.46591 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2a3b386-462f-3671-83af-b72f19e65d6c | -15.58304 | -57.47952 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bf55a6d-c101-35df-b0ba-d91ded9a499a | -10.64305 | -57.9771 | 2024-09-29 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b03dfee-d2c2-3139-868a-73a57595d43e | -10.64267 | -57.97993 | 2024-09-29 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 238731f3-4dc1-31c5-bada-4758a738fed2 | -11.72594 | -57.43903 | 2024-09-29 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 88db73d4-a33d-37df-90a8-b78202863b72 | -11.72553 | -57.44232 | 2024-09-29 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 32c77334-5969-3c95-9a3b-1874ca1ac8e9 | -14.89639 | -57.98592 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eba6ef47-cb49-34dc-b321-3e1d83b18858 | -14.8907 | -57.98869 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b39a7733-3966-3b63-bc8e-fae84f913c7d | -10.69598 | -58.53042 | 2024-09-29 05:44:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 164c6630-8a9c-3b2e-a288-a4121e983f40 | -10.69539 | -58.53097 | 2024-09-29 05:44:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0922c14f-c2c8-3bbd-897f-780d3c90a7ab | -10.69527 | -58.53566 | 2024-09-29 05:44:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3335432c-812f-3a1a-bb91-3f1c93e69ffe | -10.69471 | -58.53622 | 2024-09-29 05:44:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4032e95e-e112-3d31-82dc-72d06620674e | -10.69116 | -58.52978 | 2024-09-29 05:44:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ba6f392f-5e6d-3832-aac0-4f20eb0ddbd2 | -10.69057 | -58.5303 | 2024-09-29 05:44:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c6e81f9c-c5dd-3191-a2cb-21fa4b5eee0b | -10.69045 | -58.53501 | 2024-09-29 05:44:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3c058895-7bad-306e-bc7a-68573a94c069 | -10.6899 | -58.53555 | 2024-09-29 05:44:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f62f7e5a-1dd5-3507-bea5-db27d0e17db8 | -11.71252 | -58.89516 | 2024-09-29 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2908f1d5-be90-3813-a657-bb1e48d3f50b | -11.68843 | -59.30842 | 2024-09-29 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4fc98bc4-8ba2-38cd-af4c-bdbc68001e57 | -11.37915 | -59.13432 | 2024-09-29 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a9970db-b25b-3af4-923d-cefcb382b7c7 | -11.37447 | -59.13379 | 2024-09-29 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85711e47-8d3a-3606-bee8-cd07a46a985d | -14.52499 | -59.76843 | 2024-09-29 05:44:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2539eec0-1893-36c6-8757-5fe7fbebde3b | -10.72798 | -60.76111 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33d8f0a2-6f4b-31d4-ba54-eb75912f1f4f | -10.69228 | -60.72628 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ef6ea9f-53d7-3620-8787-c566b4ce3777 | -10.39228 | -61.17262 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5951592c-acf8-3fb5-b538-69851454a6e0 | -10.39177 | -61.17619 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95353dd2-6344-3fab-8128-ca610c0d5ed5 | -10.39127 | -61.17975 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9773d5f0-9ccf-30ed-aea4-7e30133914d5 | -10.39077 | -61.18327 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccb3b5ec-9543-3c33-be36-beaa3c64de55 | -10.39028 | -61.18678 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e3b471c-c0e0-3d9c-ac90-11048d12dbf6 | -10.38978 | -61.19028 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b884fc4-0e26-3233-bc40-72482542e773 | -10.38878 | -61.16847 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18856fd2-e30f-3677-8a9c-ec86db5523a0 | -10.38827 | -61.17202 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9675550b-a3c8-369b-a26a-ef0150327116 | -10.38777 | -61.17559 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d648f11d-9350-33a3-8fe7-f334f808a286 | -10.38727 | -61.17915 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6124ef7-fc6e-3de0-a83e-ef32e2bde867 | -10.38677 | -61.18267 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a2615db-4d98-37a5-b469-e97de6810099 | -10.38628 | -61.18617 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f858d94d-247c-3e93-ad1d-9330c4a829c9 | -10.38578 | -61.18968 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b305c6f0-3879-330f-b46d-16d18480832a | -10.38427 | -61.17142 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dab44db-69e0-3dda-bb19-f64fc20cb645 | -10.38228 | -61.18556 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 541d9164-ad84-33b3-aa55-712db4a9c59e | -10.93524 | -60.82453 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d6487649-26cf-34de-b787-e81ac90cc3bc | -10.90787 | -60.66896 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab53468d-395d-35d8-b0b0-b3d40ef3a32b | -10.90371 | -60.66829 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bffdb0e-1f63-303c-8483-29c2ba92be38 | -13.67975 | -60.71539 | 2024-09-29 05:44:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfe09e29-02a5-3382-afe4-426c6f18df29 | -10.20577 | -61.41334 | 2024-09-29 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 509a56f2-be0f-3406-98b4-be6e444387cd | -12.30702 | -62.3072 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1171edb8-7a0c-30ee-af03-5af80ef6e78f | -12.25817 | -62.34876 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b616a645-e7f9-359d-8ee4-89f18844272a | -12.25435 | -62.34819 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e5a5f756-9766-3c3a-be25-389b4a8a3734 | -12.24986 | -62.35242 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 482b9994-fb7e-3cc2-b2e4-c776ab71caf5 | -12.04532 | -62.95448 | 2024-09-29 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1951d38-6dd3-3af1-bf51-e6209f02727b | -12.99342 | -62.70007 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 04159e5c-8913-3513-ac33-d44522bc032a | -12.99276 | -62.70478 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2debcb19-f911-3132-8ee3-93e3e16bfa19 | -12.99209 | -62.70948 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e2d268d-f4ee-3f0d-802f-1c9354e8b636 | -12.99031 | -62.69481 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0d20b5b-3955-3d10-8898-dc90007ea93a | -12.98964 | -62.69952 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3aba4c78-281c-3833-8bfa-5de9478afd96 | -12.98898 | -62.70422 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ea4e1179-bd15-3255-ac01-849f5cffe255 | -12.98831 | -62.70891 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c336aa28-c210-3c9f-825a-ab001e5e4991 | -12.9852 | -62.70367 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5d15bd0a-1dc0-3a58-9f2d-7a7591648dcd | -12.98454 | -62.70835 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 17a65531-79b9-355d-a317-2c4df8cd1c9e | -12.98142 | -62.70311 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 811570f5-f1c7-3d5c-bcff-9c7cd576ec36 | -12.98076 | -62.70779 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7dc4d307-72a5-348b-be58-3146fbc8ec97 | -12.87114 | -62.71807 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 228ce86e-b134-3304-8965-627391142114 | -12.87049 | -62.72273 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d474c45b-1a92-378e-80df-cf31ac041583 | -12.86654 | -62.75068 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 052d4e21-028b-3008-877a-85f127fdeb78 | -12.86588 | -62.75531 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dde3eae3-8f4f-3141-9891-7f9038cfea3a | -12.86522 | -62.75996 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3b56b20e-a0b7-3c08-8f6c-79f474f2cfaf | -12.86391 | -62.76925 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5cc80117-fc07-3bd2-b373-72f6228cabbc | -12.86343 | -62.74546 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06ad8294-f91b-3620-b41c-770f247089a4 | -12.86278 | -62.7501 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b28c583b-28d0-37ad-acbe-44cf339d92bc | -12.86015 | -62.76868 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a100816-6a1a-3877-82c8-77e1181faaf0 | -12.8564 | -62.76812 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19aeb316-0165-3884-b41b-4c1c4fe61a2b | -12.84592 | -62.73334 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f99c3f4-dc94-3a9b-991f-6d84d33c2f65 | -12.82969 | -62.71187 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61085925-d58f-3316-853e-4a986cbb3795 | -12.81379 | -62.24249 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b6f9260-5b85-3b9a-93eb-43ba1af6959d | -12.80606 | -62.24121 | 2024-09-29 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcd17e48-39f9-3b81-978a-6f93b262def6 | -12.78924 | -62.61301 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fdbc7fe0-db1c-3604-a0d8-d9af3b46d54b | -12.78857 | -62.61773 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 882f79c5-e545-3423-9c92-49f0fe58503c | -12.78545 | -62.61245 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b5bbf6cc-4c0c-3dbd-a219-ea79ad6f1d71 | -12.78167 | -62.61189 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a3cefd1e-48ec-36cd-8781-932d5f2ce17e | -12.77994 | -62.75954 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0c53f92-e4e4-3fe2-a6da-3350eaffe792 | -12.77928 | -62.76416 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71987dfd-f753-3bc1-99ec-fb879a66b897 | -12.77788 | -62.61133 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 95010dc5-7ff4-3a99-8831-71d604192175 | -12.77619 | -62.75898 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff95a8b6-146c-3338-99c0-21604fb24295 | -12.77553 | -62.7636 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8df2983-d00c-32d4-8a37-46993eb7bc06 | -12.77487 | -62.76822 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d1e62a4-a4b7-38fb-a47a-0b6c369363b7 | -12.77409 | -62.61078 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3f34675b-3178-3a68-9fb3-0d3025c22e87 | -12.77343 | -62.61549 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c6de1cfe-e96d-382c-92ad-1dc7402a4ce0 | -12.7703 | -62.61023 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3c198e9f-5ae7-3c91-9d11-53d19367b6c1 | -12.76539 | -62.78098 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3e489d3-8396-36ce-ac71-bbecff9b5b2d | -12.765 | -62.83726 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d484d2e6-fc21-3af6-bf11-f7a4dc42dbc1 | -12.76473 | -62.78558 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26b88404-588e-39aa-aeb9-eea5caa11645 | -12.76435 | -62.84184 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae22a365-ebc2-383c-948b-6efc0b5a7946 | -12.76304 | -62.85099 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8955c892-d1a6-3d5a-a17c-e438c8f06e60 | -12.76061 | -62.84128 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 632bbf4a-ac75-38e9-9e8b-cbed8e6ff7ce | -12.76033 | -62.78962 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README67.md)
