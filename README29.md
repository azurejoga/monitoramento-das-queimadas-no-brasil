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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83cf47d0-db18-3afa-bdc6-a661ad4beb42 | -18.88358 | -41.09567 | 2026-08-20 04:04:00 | NPP-375D | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ede56388-6ae6-30f0-92e9-efcf3fe486ff | -15.3601 | -52.78085 | 2026-08-20 04:04:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7af2e868-f818-333b-88e8-4d6626edcf87 | -15.36198 | -52.7727 | 2026-08-20 04:04:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9eb6fdd-d0ca-374f-a48b-dd569b5899bc | -23.62555 | -48.28531 | 2026-08-20 04:04:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e52daa1f-2841-32be-8761-7a30a5f7e4ac | -21.44522 | -48.51612 | 2026-08-20 04:04:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d21f4cec-9131-3a35-9bf2-fa0aeef134dd | -15.36679 | -52.78319 | 2026-08-20 04:04:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e98fba6-7959-3fff-8f12-4c9b9dd85043 | -20.25922 | -46.74921 | 2026-08-20 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adc27c14-f4b1-3868-9981-018584426823 | -19.6106 | -46.26981 | 2026-08-20 04:04:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5ce5d5d-ecb7-3667-b1d5-b2b42d36132d | -15.36847 | -52.77591 | 2026-08-20 04:04:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c7c306a-50e9-31b3-b769-e240e6de4a70 | -20.26551 | -46.74043 | 2026-08-20 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3ffeef9-3706-359f-9ac2-ac02f1066a4c | -18.55618 | -48.29485 | 2026-08-20 04:04:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c9640389-c939-3d8b-a8ef-6f1f76f72255 | -18.03957 | -44.61563 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1a5f8f5e-0da8-3b3f-9d9a-26d6ce05e087 | -18.03165 | -44.62172 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 904b9d8a-c972-3f2a-9152-38adcbbbae04 | -22.34838 | -49.04875 | 2026-08-20 04:04:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aaad320c-6aa2-3463-9f8a-31811afc8bb7 | -18.04058 | -44.61802 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b0168d1a-baaa-32eb-9980-b7c08dd17a8d | -20.26456 | -46.74518 | 2026-08-20 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c1f61af-39eb-3989-8cb1-8aba7229b323 | -18.03164 | -44.61403 | 2026-08-20 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 33a31912-8507-32da-a9bf-13f8b4c8b24e | -15.37964 | -52.72735 | 2026-08-20 04:04:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47afee77-fd98-34ea-b2f0-4339f8720865 | -16.386 | -49.23285 | 2026-08-20 04:04:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0aea48ad-c539-3240-a7ca-2efe5cc31ea5 | -17.33359 | -43.62252 | 2026-08-20 04:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 2c253e1b-a97f-350a-88be-fe64b7dc37b4 | -8.654 | -54.6505 | 2026-08-20 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4c370bc4-bf55-30de-8a27-17f4040f4da1 | -9.12 | -61.6011 | 2026-08-20 04:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| f081e693-4985-3c7b-b2a5-7c1774d9e4a6 | -9.1059 | -60.9319 | 2026-08-20 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 0e4cba72-77bb-340f-a21b-44dff30938c3 | -9.2071 | -59.771 | 2026-08-20 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| f0325385-7c94-3d39-8a4e-7ea06cfd71a3 | -10.3897 | -61.2118 | 2026-08-20 04:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 58bb721a-811b-38c7-b35f-befe01e33fde | -8.6727 | -54.6492 | 2026-08-20 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 8089f74a-a172-3d55-9d3e-09debb9f996d | -2.63617 | -47.98451 | 2026-08-20 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 21686ef6-6358-39f1-8c4d-15626d5b73b2 | -4.0594 | -49.10545 | 2026-08-20 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abd10f1a-0e17-3bf4-8f62-149d7d49e087 | -2.63972 | -47.98901 | 2026-08-20 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eac000a4-d097-3f21-a270-ce9b670311f2 | -2.0476 | -48.03511 | 2026-08-20 04:17:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2912aace-a42b-3c13-84e0-8fc4e19d79e0 | -2.6759 | -51.88426 | 2026-08-20 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb952e58-f589-3cd7-9b05-942a7005f88a | -2.51179 | -49.36143 | 2026-08-20 04:17:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b0f2fac-2efd-300c-9a09-1e8194eb4030 | -2.57343 | -47.20646 | 2026-08-20 04:17:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 792751f5-b66a-3461-8ccb-21c1aeb3c277 | -2.64034 | -47.9852 | 2026-08-20 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 898a315a-0ee2-3f41-a87d-d26920987eb3 | -4.39493 | -42.34513 | 2026-08-20 04:17:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 95600969-2b6f-3583-9fd8-7a8e577ef2c0 | -4.01124 | -48.95879 | 2026-08-20 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90134727-d333-3c1c-818c-bb53c8c1437b | -3.2649 | -49.52648 | 2026-08-20 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 513d1f58-d3f0-3239-a902-3ee01fd315f9 | -0.98066 | -47.50205 | 2026-08-20 04:17:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9fb2a505-702b-30bb-aeb2-2031264ea754 | -4.28071 | -46.51629 | 2026-08-20 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e1ad4698-870e-3f9f-9248-4c580a5c883c | -2.64451 | -47.98586 | 2026-08-20 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87b30490-9559-35f7-b277-1302b1944251 | -3.53192 | -48.18371 | 2026-08-20 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7b6a2e18-ac78-37c2-b81b-210d7ca9d662 | -3.84886 | -49.04213 | 2026-08-20 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 20d315c1-e5f2-39c4-8566-f3743606de24 | -4.12441 | -49.44747 | 2026-08-20 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fa88660c-e5f7-383f-93d1-fcc46562f41a | -4.26849 | -48.19227 | 2026-08-20 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b69ae5e-fece-364c-91ea-257c1866aad6 | -3.97193 | -49.19897 | 2026-08-20 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1145ddc-723f-3c55-a335-e2db9731e2c3 | -3.97264 | -49.19464 | 2026-08-20 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4c3d49e-7bdc-3bd0-ae24-09a80624807d | -3.03804 | -48.41418 | 2026-08-20 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9724d484-a7af-3b8e-88af-76229c0c058d | -2.04696 | -48.03902 | 2026-08-20 04:17:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ace0d874-bb45-3e6e-856b-146b8c5a55ec | -2.11382 | -47.11438 | 2026-08-20 04:17:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b190e180-d4ee-35f0-b644-45b837689165 | -3.02358 | -41.16988 | 2026-08-20 04:17:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a897e475-f015-3f58-ba3e-f2cf75025d2f | -5.21206 | -42.76397 | 2026-08-20 04:17:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 83ad8d75-f3c4-3728-9233-518a87d68aa5 | -4.76909 | -41.79922 | 2026-08-20 04:17:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6f4d43e6-1538-3bc3-b39b-163338f46fbd | -3.01815 | -51.06595 | 2026-08-20 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20076cf2-f345-3219-a288-20e63255ff9d | -3.03475 | -48.41425 | 2026-08-20 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00851f8e-ebf9-3ecb-b385-5ba55c548812 | -2.82646 | -48.64972 | 2026-08-20 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7ada305-925e-3d7d-9d57-aa789559fbf3 | -3.05591 | -46.92533 | 2026-08-20 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 597334bf-dbfc-3337-983b-cd8221652df8 | -3.26567 | -49.52176 | 2026-08-20 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e760ddd-3843-3afb-9369-021808037a40 | -2.43253 | -47.03121 | 2026-08-20 04:17:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee1f6b1a-8e24-35cf-8481-a9b219affdf9 | -2.57425 | -47.20135 | 2026-08-20 04:17:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0183eb8e-a022-34ac-a32b-320389e3305b | -2.57376 | -47.24546 | 2026-08-20 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f41418fd-9979-38c0-916b-59fdfbc94535 | -3.01354 | -51.06203 | 2026-08-20 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74ed62d3-3b81-315c-90d9-5bb14357f619 | -4.7152 | -42.77044 | 2026-08-20 04:17:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8478f7a8-b431-3a4d-ba23-80906b8a3518 | -2.59239 | -47.93845 | 2026-08-20 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61722e4e-94bd-3bfe-9041-14dffb8dbcef | -2.6753 | -51.88776 | 2026-08-20 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2f35f87-8102-3d6b-856b-b79057fc3b4f | -4.71851 | -42.77095 | 2026-08-20 04:17:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19176e75-e8e9-3ea3-a339-f96a4fbd27af | -4.09532 | -42.49994 | 2026-08-20 04:17:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0f69bb99-a636-307b-bd78-31a9fbe27149 | -4.27054 | -48.19032 | 2026-08-20 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c342772-6bbf-3a7a-8e5c-d74bbf2c5915 | -1.8084 | -47.1962 | 2026-08-20 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4460b11d-5338-30cd-93ed-804a066d79b9 | -3.01403 | -51.059 | 2026-08-20 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15cf8823-5b1d-3b13-90d1-570d7530d153 | -2.80337 | -48.59135 | 2026-08-20 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f6179d4-b110-37f9-952f-c5f23fc8ec7e | -2.56693 | -47.24732 | 2026-08-20 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0fe6a568-5d50-3b33-a81a-5022699c168d | -4.09477 | -42.50338 | 2026-08-20 04:17:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 366f3582-5772-3dc2-b753-3ceb8e3fc29c | -1.82404 | -47.89268 | 2026-08-20 04:17:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce9d8370-c2c1-39bf-b09a-10b73e347cd7 | -3.47419 | -47.70016 | 2026-08-20 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c886fb7-4bec-3bcd-a583-fd26270e6dec | -2.56612 | -47.25242 | 2026-08-20 04:17:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aec702ed-92c1-3d07-83cf-afb4cd9da640 | -2.79071 | -49.52184 | 2026-08-20 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab523332-744c-3332-90e4-97c199e38cdb | -2.57091 | -47.24794 | 2026-08-20 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5556eb88-5597-3f8a-a112-0674943bc3ae | -2.16706 | -47.48275 | 2026-08-20 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d60bda71-0ac2-3a6e-8156-84aa86eb593a | -4.39162 | -42.34462 | 2026-08-20 04:17:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| af27a8a7-20aa-38d5-bdfc-b3ebea9218a4 | -2.57172 | -47.24287 | 2026-08-20 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 63cc4721-daa2-3b89-b075-d655dec88d97 | -0.97651 | -47.5014 | 2026-08-20 04:17:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d98c77c-8764-3a6a-b40f-de4eb1cf06f5 | -2.57252 | -47.23782 | 2026-08-20 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 014f1483-3cb2-3620-83b8-09d9d89c398d | -3.53609 | -48.18435 | 2026-08-20 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b130a1f9-dfe8-31ec-bae2-efa5800642f1 | -4.39548 | -42.34167 | 2026-08-20 04:17:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4e2382b1-fe6e-3bc1-b10c-5da927a74791 | -2.83081 | -48.65045 | 2026-08-20 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdd0919b-83c2-33f0-ad9b-98a3edd82706 | -3.56269 | -43.20266 | 2026-08-20 04:17:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1a1492c3-39c8-3e01-8f65-8be09f204083 | -2.53951 | -47.16452 | 2026-08-20 04:17:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 675497e8-808d-3255-a432-72f904b0beb3 | -2.5746 | -47.24041 | 2026-08-20 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c250c259-0024-33bf-988d-65848a391564 | -2.76637 | -48.57248 | 2026-08-20 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7523d27-d560-3366-bb77-fe0467020c01 | -4.09586 | -42.49649 | 2026-08-20 04:17:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b4e37567-8ca7-3b39-a821-1cb3f28e282f | -5.12397 | -40.59377 | 2026-08-20 04:17:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2a41692a-9f2b-3f41-858e-adaad49155df | -2.80501 | -48.59079 | 2026-08-20 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 772e6fa4-e862-3e61-8491-1bd0312bb764 | -3.02694 | -41.1704 | 2026-08-20 04:17:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c87995ed-f6ba-30b5-91f6-4309f98ecda3 | -4.57706 | -44.74742 | 2026-08-20 04:17:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 92dea09c-6776-3817-9b2d-31a43889ec31 | -4.12891 | -49.44826 | 2026-08-20 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66f31440-f19b-3c22-a159-1d8def960ae5 | -3.0275 | -41.16683 | 2026-08-20 04:17:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d1f0e3a3-0304-374b-928f-3c82dd65202b | -4.9349 | -41.97992 | 2026-08-20 04:17:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b76ba02e-4b9d-3b0f-8fe0-43a1de61c9e5 | -4.09146 | -42.50286 | 2026-08-20 04:17:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0cf88f35-7f04-35eb-a138-a19afa49afa6 | -4.93435 | -41.98343 | 2026-08-20 04:17:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 20d296d9-f42f-3ce1-ab5f-d46ae17fd2f8 | -3.45245 | -39.26119 | 2026-08-20 04:17:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README30.md)
