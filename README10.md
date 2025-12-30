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
| 5b8e2e81-2c43-3117-aa1f-cac45d3e1ed7 | -7.38919 | -40.54716 | 2025-12-30 11:57:00 | TERRA_M-M | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 011d546c-2832-3949-bdba-bcf320afd4db | -7.60681 | -42.02827 | 2025-12-30 11:57:00 | TERRA_M-M | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| b782ff36-bdc9-3dc4-aca0-aa2433d8668a | -7.39076 | -40.53568 | 2025-12-30 11:57:00 | TERRA_M-M | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 147630c7-dab2-3b6f-8c26-e3d8578e8c4e | -11.00367 | -44.34095 | 2025-12-30 11:57:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a7c6a5e0-f976-385a-b9c8-70eb7fbd4efd | -13.93305 | -41.44492 | 2025-12-30 11:57:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 6ff7f2aa-9582-3528-9569-e849fbf83cdf | -12.66769 | -46.77096 | 2025-12-30 11:57:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 0bb9ec73-79eb-3700-baf6-51ebde7c9c17 | -7.39856 | -41.00434 | 2025-12-30 11:57:00 | TERRA_M-M | BELÉM DO PIAUÍ | PIAUÍ | Brasil | 2201572 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 62995f62-9668-3d38-bd17-42a579a62f16 | -12.82715 | -43.0945 | 2025-12-30 11:57:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 0d5f9bc7-743e-3c67-a1aa-e3ffa1583de3 | -7.87223 | -38.55917 | 2025-12-30 11:57:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 0b80c2a0-47ff-3d71-b781-30cc0fe97fc6 | -8.30128 | -39.48369 | 2025-12-30 11:57:00 | TERRA_M-M | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 13.7 |
| e88a7e99-2ea4-31b3-be48-ad99716551cb | -8.19223 | -36.42793 | 2025-12-30 11:57:00 | TERRA_M-M | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 43.4 |
| 4946616d-30a0-30a3-9d2a-6958a121191a | -7.60814 | -42.01863 | 2025-12-30 11:57:00 | TERRA_M-M | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| db5fc575-2e0d-3fa8-b5d1-4d02e0df4b65 | -11.78066 | -44.19026 | 2025-12-30 11:57:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 199.6 |
| fe05e5fb-0b7d-3c6f-af7b-c7be5926a055 | -11.82593 | -46.59517 | 2025-12-30 11:57:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| e24864fa-3a81-374d-813b-e778d18d8f7e | -11.76393 | -43.3288 | 2025-12-30 11:57:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| f232f118-f2e4-3cd8-9a92-9de619e821fc | -11.15761 | -43.44808 | 2025-12-30 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 43aaef42-e058-341b-b47e-995dc7660318 | -10.36397 | -40.28693 | 2025-12-30 11:57:00 | TERRA_M-M | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 011524b9-a574-31ce-9555-c8f19d6a46b8 | -10.19504 | -44.89598 | 2025-12-30 11:57:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 359fd4af-fefb-32e3-89ca-b75b4d799207 | -13.80829 | -42.9243 | 2025-12-30 11:57:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 52c0b326-9986-3e1e-9c0e-534ed5bf5b6c | -14.34867 | -42.86699 | 2025-12-30 11:57:00 | TERRA_M-M | CANDIBA | BAHIA | Brasil | 2906600 | 29 | 33 | nan | nan | nan | Caatinga | 56.4 |
| c3e66349-1746-3949-96e9-4c02a6a210a3 | -9.60323 | -40.5638 | 2025-12-30 11:57:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 491c9afd-ef4e-3526-a564-8ca330ee07e1 | -13.40961 | -43.01001 | 2025-12-30 11:57:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a095d2a0-fca2-30ad-8a03-911ad547b92d | -15.7861 | -43.65965 | 2025-12-30 11:59:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e52b1a76-4625-3138-9e67-699a32f06132 | -17.20512 | -44.32265 | 2025-12-30 11:59:00 | TERRA_M-M | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9a1ade9e-6c31-35c9-9fda-90ad3d1b1f6e | -18.45311 | -44.47824 | 2025-12-30 11:59:00 | TERRA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 80e857bc-b31c-3a53-90c3-49ce2ae859ef | -18.35543 | -44.09849 | 2025-12-30 11:59:00 | TERRA_M-M | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d6747e3a-95a2-3c9d-be73-4efccb0e9f65 | -14.3851 | -47.36646 | 2025-12-30 11:59:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4517a296-8ace-3bb9-8fdc-4f2b2b9a7af0 | -16.75576 | -42.64961 | 2025-12-30 11:59:00 | TERRA_M-M | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 01a36bf2-9199-306b-a440-bd9e748bf3ad | -20.67128 | -44.93611 | 2025-12-30 11:59:00 | TERRA_M-M | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 35883794-19cf-3ffb-84ab-4954a46d7587 | -15.67707 | -46.70218 | 2025-12-30 11:59:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| aa4ea7f8-34cb-3a11-bc97-e0661be9caab | -16.02942 | -43.49998 | 2025-12-30 11:59:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5c286f65-fa54-3917-a9b2-3b882646e281 | -22.19134 | -47.05341 | 2025-12-30 11:59:00 | TERRA_M-M | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6fd612c4-8713-3385-b9b8-562b12deaece | -16.73203 | -42.59913 | 2025-12-30 11:59:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a57c0192-faf0-3649-8982-a27b4d0c8f54 | -20.6314 | -43.18291 | 2025-12-30 11:59:00 | TERRA_M-M | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 0e0eef74-4292-3e3c-a921-cf084e312a92 | -17.32163 | -43.64764 | 2025-12-30 11:59:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b46fc64e-c3c6-33b1-bc2e-0fa37e58984a | -23.03863 | -48.6736 | 2025-12-30 11:59:00 | TERRA_M-M | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9388fcf2-c3b0-34c1-b63d-7b168937e5c7 | -19.58752 | -42.64979 | 2025-12-30 11:59:00 | TERRA_M-M | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| b2be7312-32b1-31de-b24a-729d6c1de4e8 | -18.77105 | -42.66795 | 2025-12-30 11:59:00 | TERRA_M-M | VIRGINÓPOLIS | MINAS GERAIS | Brasil | 3171808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 48a1de03-3162-3958-b3e5-bed3cb8922c1 | -16.03616 | -43.49697 | 2025-12-30 11:59:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d6948da4-ea2c-341e-a482-625eaa64efdc | -15.13607 | -45.2838 | 2025-12-30 11:59:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c061e7a0-a7a5-33e3-b3d8-b3e1f0b47f72 | -17.40188 | -45.87923 | 2025-12-30 11:59:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 505d9063-afec-3f48-ad74-52c02787c6e9 | -15.50148 | -46.64253 | 2025-12-30 11:59:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e4a14cba-4860-3802-95a5-5f9c736f8d1a | -18.45177 | -44.48817 | 2025-12-30 11:59:00 | TERRA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 42.9 |
| b7e9a10e-f538-3fa0-b005-0df6e4a77cc3 | -17.57249 | -46.54768 | 2025-12-30 11:59:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| afb8ba43-b3cc-3e5a-b30f-5e167882fea2 | -20.03839 | -43.28606 | 2025-12-30 11:59:00 | TERRA_M-M | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 123bb858-b315-3884-890f-c70387a7a8d4 | -7.4511 | -38.3365 | 2025-12-30 13:10:00 | GOES-19 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 42ec7e43-ed55-3ac1-8e05-135cd656d204 | -3.8884 | -42.5446 | 2025-12-30 13:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 8e9acd17-fe91-340d-ba73-d86f9f76dd25 | -3.8882 | -42.5682 | 2025-12-30 13:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 8f664202-c385-3e5d-a85f-edc6833cc66c | -11.7594 | -43.2898 | 2025-12-30 13:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 6e3f6d3b-932f-3c88-a292-4611dd0ab716 | -3.5461 | -43.5894 | 2025-12-30 13:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 155.4 |
| e9d7eba5-5243-3d22-b291-4d2a02d0e14f | -6.112 | -41.2649 | 2025-12-30 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| f58d035e-9efd-3634-a7ea-a91b2177127f | -3.8882 | -42.5682 | 2025-12-30 13:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| cbfca42b-08b2-3860-8249-9e1831a6f0b4 | -3.9069 | -42.5672 | 2025-12-30 13:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 40efcdd2-6845-384c-affd-5a77b5267cf1 | -11.7589 | -43.3136 | 2025-12-30 13:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| c989364d-620f-32cd-971e-6fedb290e776 | -3.5461 | -43.5894 | 2025-12-30 13:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 4b973a01-895a-3655-98bc-4ef6b70cab1c | -8.3672 | -36.8854 | 2025-12-30 13:40:00 | GOES-19 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 128.5 |
| e6818954-468a-3386-a6e2-2d6298794f7f | -11.7589 | -43.3136 | 2025-12-30 13:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 160.8 |
| b86b2e8d-5a17-398d-8e1d-9791b182b792 | -3.8882 | -42.5682 | 2025-12-30 13:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 122.1 |
| 9c941c41-af10-3635-8fe3-fa5fffe67132 | -3.8884 | -42.5446 | 2025-12-30 13:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| c8df0baf-2e69-341f-9063-12ca6e155a17 | -11.7589 | -43.3136 | 2025-12-30 13:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 37227383-873d-38ca-9e0c-b08901893503 | -11.7594 | -43.2898 | 2025-12-30 13:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 122.1 |
| 018eb366-cbfc-3bbb-8eb5-77a80f3ec23e | -3.8884 | -42.5446 | 2025-12-30 13:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 8edb4af3-2ca7-320d-be5c-9d637da92dc4 | -7.581 | -37.1781 | 2025-12-30 14:00:00 | GOES-19 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 126.0 |
| 57cdd707-6708-379c-9b4b-a7d530eaff96 | -3.8884 | -42.5446 | 2025-12-30 14:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 6cf18da6-24d8-31c1-8e86-e6d20c396987 | -3.334 | -41.431 | 2025-12-30 14:00:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| a96523b8-2cc8-3cc8-9126-b9338c612b41 | -12.6745 | -46.7605 | 2025-12-30 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 153261c9-4c95-32ac-bd1a-27546560ae73 | -11.7594 | -43.2898 | 2025-12-30 14:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 127.2 |
| 0ac67781-2b85-34ee-9a94-18254fa254ac | -3.8884 | -42.5446 | 2025-12-30 14:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 8da17495-61e0-38ce-86e8-060a8e2a957d | -12.6553 | -46.7633 | 2025-12-30 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 4a94b1a9-0ba2-39ef-9b95-42e3c6218035 | -7.8323 | -35.6212 | 2025-12-30 14:10:00 | GOES-19 | BOM JARDIM | PERNAMBUCO | Brasil | 2602209 | 26 | 33 | nan | nan | nan | Caatinga | 110.2 |
| f56efd2c-3450-3cc3-9521-ae22e33cf058 | -7.9418 | -37.2615 | 2025-12-30 14:10:00 | GOES-19 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 123.4 |
| 21a65493-fe83-3e18-b22c-52ea1747f0ae | -7.9418 | -37.2615 | 2025-12-30 14:20:00 | GOES-19 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 118.9 |
| 38cc1bcc-1593-3ea7-82d8-180a4950686d | -7.8323 | -35.6212 | 2025-12-30 14:20:00 | GOES-19 | BOM JARDIM | PERNAMBUCO | Brasil | 2602209 | 26 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 8b475440-5d87-3b86-b24e-ccf49525766e | -3.8884 | -42.5446 | 2025-12-30 14:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| b5633dca-efc7-3eee-87d7-6fcc494e357b | -12.6745 | -46.7605 | 2025-12-30 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| dabeb436-9d9c-3fdc-b20d-a0fbf115643f | -12.6553 | -46.7633 | 2025-12-30 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 24d5287b-ab52-3f1b-85c7-f96786eafd21 | -12.6553 | -46.7633 | 2025-12-30 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| e5c19890-9431-3949-bd99-8b5adaf2d9f9 | -7.9418 | -37.2615 | 2025-12-30 14:30:00 | GOES-19 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 121.5 |
| bc6a5421-d870-34a8-a286-dc0f2571ceff | -3.8884 | -42.5446 | 2025-12-30 14:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 0dc969ed-938f-300e-acc5-f132e7ede821 | -7.8323 | -35.6212 | 2025-12-30 14:30:00 | GOES-19 | BOM JARDIM | PERNAMBUCO | Brasil | 2602209 | 26 | 33 | nan | nan | nan | Caatinga | 123.5 |
| bb906f45-b9e0-3a28-9803-bf9dc9586545 | -3.334 | -41.431 | 2025-12-30 14:30:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| e25737d1-2885-3e32-9e16-410688d81117 | -12.6745 | -46.7605 | 2025-12-30 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 7672d90a-4523-3667-b8a9-2944fd782e7c | -11.7589 | -43.3136 | 2025-12-30 14:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 8fe01535-7665-3357-8708-2ceae0ebbeab | -3.334 | -41.431 | 2025-12-30 14:40:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 100.4 |
| 3691857b-f6d0-3a7a-8c8f-8bcb1dfc9ec4 | -3.8884 | -42.5446 | 2025-12-30 14:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| 5cf0a182-9be5-37ca-aa58-c285f1025934 | -12.6745 | -46.7605 | 2025-12-30 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 9c4b7901-eae2-3a10-8bdc-ec5dcb7c561f | -7.8323 | -35.6212 | 2025-12-30 14:40:00 | GOES-19 | BOM JARDIM | PERNAMBUCO | Brasil | 2602209 | 26 | 33 | nan | nan | nan | Caatinga | 142.9 |
| 454e01ee-a99b-38c8-b06f-9e9c3eeb80e0 | -12.6553 | -46.7633 | 2025-12-30 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 759dd60f-8ffa-31c5-a5e3-38a73e44bd25 | -4.7153 | -42.0451 | 2025-12-30 14:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 122.6 |


