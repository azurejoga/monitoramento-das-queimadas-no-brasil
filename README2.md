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
| 130f3f0b-1204-35a3-97fe-d75adea8a9dc | -4.9102 | -43.4666 | 2025-10-15 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 282.0 |
| da8a960d-70e1-3388-913f-37c9b46ec3c0 | -4.8915 | -43.4678 | 2025-10-15 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 282.7 |
| 1eb5b367-00b2-333b-89ed-a51ad26e083f | -4.8916 | -43.4446 | 2025-10-15 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 208.5 |
| fa559842-9211-3a22-bb33-a72ab094eb97 | -12.9376 | -47.0823 | 2025-10-15 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| d174860d-3780-317e-95d9-f87c4fbb3772 | -4.6511 | -43.1104 | 2025-10-15 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 6f188ba8-c0d8-3901-ba7e-cc2c2d907a1c | -14.2428 | -51.6079 | 2025-10-15 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 729a359c-1ada-3436-89ca-89121c44c998 | -8.7404 | -43.8659 | 2025-10-15 00:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 4dd2bfcf-2689-322a-a327-d1aca2d66b90 | -7.9442 | -44.115 | 2025-10-15 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 2450165a-0580-3e12-9b48-c77d766fa4e1 | -14.2431 | -51.5865 | 2025-10-15 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| af7365ee-3faf-36c7-856d-1fd377c25fd5 | -4.6696 | -43.1326 | 2025-10-15 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 7d712c02-4046-3b32-afe7-8efa37027b07 | -3.6674 | -45.2285 | 2025-10-15 00:30:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 106.8 |
| ea9cbcc1-c560-377e-af30-736d0f7cf1ec | -4.6698 | -43.1092 | 2025-10-15 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 57da6133-8279-3005-9298-2c42ecf08aab | -12.9183 | -47.0852 | 2025-10-15 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| c6acbda8-eba9-3dd1-8bef-c95c1a66984c | -4.9104 | -43.4434 | 2025-10-15 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 201.6 |
| b199d723-e1da-38d6-95e4-b28ec4bf71fa | -3.686 | -45.2276 | 2025-10-15 00:30:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 49955e9a-4eff-3c3b-a9f2-191b5b456339 | -12.9179 | -47.1078 | 2025-10-15 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 2269c7a0-06eb-3268-bbd7-a4baf7158ccf | -11.0626 | -51.009 | 2025-10-15 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| f9eed6db-ac5d-3fdd-9d33-5ed6192890e1 | -10.2116 | -36.6933 | 2025-10-15 00:30:00 | GOES-19 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 4904093f-0810-31b6-b451-9e3002c0614e | -3.0796 | -47.7293 | 2025-10-15 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| cd09d320-a930-3d5e-a585-ec5d425f0eba | -12.9372 | -47.1049 | 2025-10-15 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 4134440b-970b-3545-bfff-0051ef3ec5e8 | -7.9628 | -44.1362 | 2025-10-15 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 8e91f88f-c8d7-34d6-b3a1-e08243e0cae4 | -4.6509 | -43.1337 | 2025-10-15 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 214.5 |
| 8d1e52a8-6f70-3844-8390-b6de281962fb | -8.7215 | -43.868 | 2025-10-15 00:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| cf316294-3435-348c-93b7-d502f5128676 | -18.20405 | -50.74199 | 2025-10-15 00:30:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 59d6cff7-f69a-307f-94d7-051aed399608 | -18.19385 | -50.74353 | 2025-10-15 00:30:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 214a938e-c8e0-3905-b33f-7f06893f9843 | -20.43219 | -50.13996 | 2025-10-15 00:30:00 | TERRA_M-M | VALENTIM GENTIL | SÃO PAULO | Brasil | 3556107 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 96c3d003-fdda-3b9e-96be-24feee00058b | -10.87708 | -47.94163 | 2025-10-15 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 7bad264d-efcc-3f8e-8e5a-8411ff8af8a2 | -17.25904 | -46.79063 | 2025-10-15 00:33:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35a86650-ed79-3bfa-8fe4-8abc7fe4e116 | -10.46857 | -49.38639 | 2025-10-15 00:33:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ca1298a9-69a2-39b9-a05a-de80bf814dd8 | -11.51849 | -48.23559 | 2025-10-15 00:33:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3ffa2ef6-8734-329b-8612-5c206f2ec895 | -15.41848 | -42.00822 | 2025-10-15 00:33:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.2 |
| d35e6e7a-7e2a-36f3-8ef8-ff778f14e429 | -10.1536 | -46.88 | 2025-10-15 00:33:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad707b6c-92b9-3c48-864c-2f27c9437851 | -10.0506 | -43.83009 | 2025-10-15 00:33:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 8358f7ee-4256-3523-9d96-973400c6f559 | -11.48024 | -48.96619 | 2025-10-15 00:33:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bd91f2e8-f5bf-3972-aad8-2c7a489e5e40 | -12.92388 | -47.09494 | 2025-10-15 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| d335b44f-1ee2-305e-b8d4-e09d9d188bbf | -10.18198 | -49.51008 | 2025-10-15 00:33:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 165c9f43-14cd-3c34-b9ab-954808098cff | -9.96328 | -48.52724 | 2025-10-15 00:33:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7a19cdb7-1ffe-3d38-8d00-fafe33dec91d | -10.05355 | -48.7082 | 2025-10-15 00:33:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 5f984875-270f-3349-bb5c-7e07b39bb65b | -11.64487 | -47.56759 | 2025-10-15 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a60531c9-214f-3b8d-b43f-e54368842dab | -12.92522 | -47.10426 | 2025-10-15 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| d574d377-5c8f-30d1-bc80-1c8b54e68689 | -11.64359 | -47.55853 | 2025-10-15 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ca2c9953-360b-3c50-abf7-dc693dcb2b01 | -10.84033 | -47.93782 | 2025-10-15 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c191781c-9cf1-31c8-ab11-33a77cb3ec07 | -10.80917 | -47.92052 | 2025-10-15 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ab67813e-f5d0-3989-a8a4-6b7313b9eb98 | -11.0909 | -51.16067 | 2025-10-15 00:33:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 33fe79b7-080f-3fc5-9e52-c97a65a09b0e | -14.24938 | -51.61731 | 2025-10-15 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 18b67119-d4c6-3e05-b62b-75f9a198d3d6 | -12.2651 | -50.21919 | 2025-10-15 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 161c2818-e3f0-3101-9b51-72459ec86232 | -10.19085 | -49.50882 | 2025-10-15 00:33:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f5588aff-1649-3d59-9757-73fcb9f459a8 | -11.52388 | -49.15305 | 2025-10-15 00:33:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| aa2aed44-4804-30c8-8a33-6c2bffd62ef6 | -10.91636 | -47.96353 | 2025-10-15 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 65c6f1ca-ebb0-38fb-b398-f653b5170309 | -11.60863 | -48.56044 | 2025-10-15 00:33:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 20f708b4-54f5-3521-bffc-4c258b0a426c | -12.94314 | -47.10168 | 2025-10-15 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| d054b811-720c-3129-a37b-f0e6697ebc58 | -12.94185 | -47.09261 | 2025-10-15 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 425af263-97e5-3158-993d-9a8de34062f2 | -12.11082 | -49.33892 | 2025-10-15 00:33:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0e00266c-c31c-38bc-9ef3-9fd4b7e046f5 | -10.96022 | -47.94129 | 2025-10-15 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 858d40a2-45dc-3cb1-b7ee-71d0a6045dc5 | -11.56586 | -44.08246 | 2025-10-15 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 25dc7573-437a-349e-8387-3303f784d21b | -10.20307 | -50.69495 | 2025-10-15 00:33:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b3e485ee-35dc-399b-a390-fff5d36e0dd4 | -10.9151 | -47.95449 | 2025-10-15 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3c8e6058-942a-37ce-a3a0-0778db7e53d6 | -10.03872 | -43.82203 | 2025-10-15 00:33:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 28.7 |
| e6ba5df7-4c42-30c3-b5bc-c388ccfa9b6d | -11.52264 | -49.144 | 2025-10-15 00:33:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 85b3390a-0250-31d8-95b0-4249340b0eae | -10.04473 | -48.70947 | 2025-10-15 00:33:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 46024a3a-225d-3775-b618-e0d351d9fe60 | -10.08784 | -49.02106 | 2025-10-15 00:33:00 | TERRA_M-M | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 652ea932-bdfd-3169-8da2-50bda8fe32b7 | -11.05825 | -47.58884 | 2025-10-15 00:33:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9db186a1-5035-33ab-8512-e39ff31bc601 | -10.61888 | -47.42049 | 2025-10-15 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 49439a98-a0cc-3bdf-b445-6391036acd46 | -12.93288 | -47.09386 | 2025-10-15 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 5b47fdd8-ef26-355e-817d-ccae696dfe28 | -10.09089 | -48.18586 | 2025-10-15 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4ee3115d-8c68-3a1d-95b1-bfe3ca648c05 | -10.04101 | -43.83721 | 2025-10-15 00:33:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| ed43329d-be42-34f8-ae1f-acdbb1e5b3bc | -10.90242 | -47.92858 | 2025-10-15 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c45defb3-f4d8-3317-aae2-6ebb5fb42024 | -12.26639 | -50.22905 | 2025-10-15 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5d8cd4e2-30d2-38ad-8c73-38b304079d09 | -10.28692 | -48.00045 | 2025-10-15 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b5bb19b0-17c1-3d1d-a3eb-6e536efd14f1 | -12.24374 | -49.3641 | 2025-10-15 00:33:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 74a6d28e-87f0-3270-ace6-97d06318e05a | -12.93419 | -47.10301 | 2025-10-15 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 3c180cda-2faf-3325-957e-42a6ad1b31e3 | -14.5388 | -41.54234 | 2025-10-15 00:33:00 | TERRA_M-M | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| fc231511-02eb-3406-87be-6b032b7e0461 | -10.90727 | -47.56725 | 2025-10-15 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d81bfab1-22a0-3898-9364-fa3ae8679411 | -11.63137 | -48.52973 | 2025-10-15 00:33:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c7cd0793-63fc-3174-b8c7-e71dd99b1054 | -11.07065 | -51.00353 | 2025-10-15 00:33:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 38.3 |
| a445655e-ad91-3345-ae2b-5ed499e2a0ba | -14.23754 | -51.60622 | 2025-10-15 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 49ffcddf-42d9-3747-84d4-7625b743bd89 | -11.05691 | -51.01131 | 2025-10-15 00:33:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ccbab583-25a9-309a-8419-36dd8cb836b1 | -10.87836 | -47.95074 | 2025-10-15 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 79b6834c-b4cb-3a3d-997c-d1d48f762897 | -15.11272 | -42.46565 | 2025-10-15 00:33:00 | TERRA_M-M | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 7641729f-2f3f-3154-9bc4-9dc5c40edc02 | -15.42134 | -42.02549 | 2025-10-15 00:33:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.6 |
| bdb8679b-fcc0-394b-9650-940d5315bd37 | -10.61755 | -47.41117 | 2025-10-15 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bfd14607-5b72-38c7-a593-35e25ae4cf9b | -16.42269 | -46.55016 | 2025-10-15 00:33:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 076f1808-b7f2-339c-90df-6ee25c803cc4 | -15.1153 | -42.48138 | 2025-10-15 00:33:00 | TERRA_M-M | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| 9c972747-d31b-3cec-b2fa-54883dd21687 | -11.59981 | -48.56172 | 2025-10-15 00:33:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| fb028015-22a4-3841-b9b1-5b5974ad54d2 | -11.28915 | -48.25115 | 2025-10-15 00:33:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 034bb23e-1fc3-3374-a220-d0487efbae84 | -10.18321 | -49.51911 | 2025-10-15 00:33:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94f58c85-23a4-363f-aa91-8cedc0df053a | -9.81162 | -47.64288 | 2025-10-15 00:33:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ecd1383b-df2b-3ff7-b650-65066081c9d1 | -9.25777 | -44.36699 | 2025-10-15 00:33:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 40b4417b-b289-32d6-9220-c00344171ce1 | -11.06252 | -51.01521 | 2025-10-15 00:33:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 641336fb-d112-3480-9834-61dfeca8fd22 | -13.00122 | -48.77169 | 2025-10-15 00:33:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 212f67c5-d484-3ef3-9728-c8e4d5646200 | -11.63013 | -48.52077 | 2025-10-15 00:33:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 127e2ed2-ecf0-32d9-9232-93574dd2657e | -9.81029 | -47.63359 | 2025-10-15 00:33:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c645ef21-4bd3-354c-8d78-0134393495a9 | -14.2478 | -51.60487 | 2025-10-15 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 0839c8ca-ba62-3679-8c6b-1ca91f0a1cd0 | -11.06118 | -51.00483 | 2025-10-15 00:33:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| b254a7bd-e6f9-37d9-9e26-b72772619c38 | -11.07199 | -51.01391 | 2025-10-15 00:33:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9fad5e0f-24b7-3ee9-923b-f9f466cf8331 | -11.6383 | -47.85361 | 2025-10-15 00:33:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 2d949c6a-f057-3576-9421-358d8f566f49 | -10.41334 | -48.17809 | 2025-10-15 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cecfa4c0-0eb8-363b-b855-56f7f898cf61 | -10.03925 | -43.83185 | 2025-10-15 00:33:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| c755208a-1c61-36ba-bbe1-e1d8dc90c9a7 | -12.91508 | -47.10199 | 2025-10-15 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| e091dc79-56a9-3c99-9b55-d3aa9c729663 | -11.00858 | -48.69059 | 2025-10-15 00:33:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |


[Clique aqui para ver as próximas entradas](README3.md)
