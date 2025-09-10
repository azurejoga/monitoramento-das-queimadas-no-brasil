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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ded6e183-c60e-3bc8-8f14-46ef223575d8 | -17.24052 | -46.07487 | 2025-09-10 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d52ca931-f703-3fba-a967-820443171beb | -12.60422 | -56.96626 | 2025-09-10 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50d5ed8c-e98c-336a-aaa9-76b3f4270c3c | -18.1302 | -51.72016 | 2025-09-10 04:44:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ff702e3-287a-347e-98c0-b91316d59a9f | -15.0881 | -50.07566 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f645332e-d760-3375-a0f2-e6bd29f8f2c0 | -11.28933 | -53.95201 | 2025-09-10 04:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87860cbc-c69a-3536-b350-dc5e90dbe063 | -16.07385 | -50.48858 | 2025-09-10 04:44:00 | NPP-375D | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dca4d509-bc7f-3515-a8fd-38ab9a10d11f | -18.52681 | -43.28029 | 2025-09-10 04:44:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fdcf80cc-8353-3771-bd0b-7f8fecb5535e | -12.97146 | -44.0163 | 2025-09-10 04:44:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d34e06f9-e93f-3464-9321-f5d70eda753d | -13.9657 | -48.22249 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6c2e72c0-e96a-31a2-b8d1-a075a7995804 | -17.20404 | -50.15923 | 2025-09-10 04:44:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 611723f9-b330-37a7-8140-21b04897b3cc | -18.31118 | -49.3323 | 2025-09-10 04:44:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa8caded-13fe-371c-97aa-041c5a79d1c0 | -14.90074 | -50.11468 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50f01d9a-5239-30a3-9795-edc763a9829f | -11.93851 | -51.07573 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b61cc3ff-6410-394a-9e2e-301618ca52bb | -13.02844 | -48.01938 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5adbbaff-4610-3955-b3ec-8ab3c6fa4066 | -15.80308 | -52.25766 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57593784-c479-3af3-9bee-07dca2946f33 | -15.57837 | -49.21858 | 2025-09-10 04:44:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1e22c31-0b05-3d3c-968e-78e86d044b01 | -14.57828 | -51.40779 | 2025-09-10 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2fe41f5-66a7-326f-897a-01ca3feff2ae | -13.00227 | -48.01336 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64cafee1-62a3-34b3-8ab3-c8f6eeb54edc | -15.51499 | -52.76466 | 2025-09-10 04:44:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d9977d1-d062-3878-8d60-f46dc5e4f83a | -12.01614 | -50.99026 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 10118e25-9620-3924-af70-81e239c0147d | -16.48474 | -51.97229 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c23b50a6-1de1-3d47-988f-4efcfdbfe41c | -15.13614 | -52.38755 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fd65605-228c-36c4-8dab-e65d2834364b | -16.51224 | -55.13849 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6235a67d-b38d-3e9d-9fcb-d07c2dacb7f3 | -14.85987 | -49.53136 | 2025-09-10 04:44:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28fa0805-22d3-3359-8e15-7635f207b71c | -11.21041 | -54.9888 | 2025-09-10 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c0dadb22-e80b-308f-91e5-0204ba00eaff | -16.57268 | -49.22543 | 2025-09-10 04:44:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| df487215-41a3-374b-b16f-56ee4ecbab7c | -16.04341 | -49.97644 | 2025-09-10 04:44:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e429e43-abbf-3eed-be4a-f222133a1af1 | -17.15902 | -50.15582 | 2025-09-10 04:44:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67aa9818-a4f4-3ccf-91ad-8f7260022440 | -13.18722 | -47.25477 | 2025-09-10 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| de5dd519-5ed1-3966-b905-dbd2ab08a239 | -15.65277 | -49.93519 | 2025-09-10 04:44:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81ca1ae7-50e3-3ee1-9efb-d07287d8b2dc | -17.3066 | -46.75813 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c517c2d-b3fc-3ee2-b8cc-16deea4f8f12 | -17.74884 | -44.48063 | 2025-09-10 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8cb8f5ed-05bd-3531-ba3e-6695e3ee2a54 | -15.17725 | -47.95079 | 2025-09-10 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5e83974-1c80-3c88-9907-158788f90cd2 | -16.44971 | -51.97745 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fab6b325-25b6-36c3-a88b-4636186a13f3 | -14.60304 | -52.10006 | 2025-09-10 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70b28570-9e9c-37fc-828f-1745a521e642 | -11.2204 | -55.00075 | 2025-09-10 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44761fc7-3810-3445-8586-dff3131a168d | -19.87201 | -48.12308 | 2025-09-10 04:44:00 | NPP-375D | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83b51702-c88a-348d-aec6-0ba9d75e7f2a | -16.67126 | -48.51797 | 2025-09-10 04:44:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 804421e6-e5a6-3852-9d4f-5aeea1acc1f8 | -13.29842 | -51.71656 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3633a61b-af5c-3f4c-a271-99b0cea0dab7 | -14.92662 | -50.10378 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 58087a47-c4e9-30f7-ba04-a87246d9879f | -12.01033 | -50.9895 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ad83e8af-7332-3e0f-878f-a29a5c47806a | -15.10562 | -50.09721 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 057c9049-391f-350e-bddd-6f5ad4d0466e | -12.92925 | -54.79883 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f28043c-3498-3e45-9f0c-44edb555b1b8 | -15.6607 | -49.92885 | 2025-09-10 04:44:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b513f01e-423c-3ddf-8d54-61e8307a3408 | -12.83678 | -52.94348 | 2025-09-10 04:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 29840399-aeda-3f4c-89d1-786f0de95743 | -13.64482 | -46.98393 | 2025-09-10 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb32d4b0-f2a1-3e57-8d5e-b917534cd002 | -18.01281 | -47.12852 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 360369b9-6769-32fe-98ac-6a12254d8280 | -18.0029 | -47.11082 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31798df3-a221-3020-be84-6bbb8191134d | -17.74825 | -44.48544 | 2025-09-10 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 457c6c3b-3d08-34b7-b610-a6f8f1717df1 | -16.62492 | -49.7714 | 2025-09-10 04:44:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 549b4b47-8c86-3996-b633-1a1e7e618bcd | -12.9073 | -47.98737 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a652429d-6b98-349f-92cc-5f176ec7db5a | -14.9255 | -50.11111 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 725b6f87-1667-34e8-bc43-265cdd98bea9 | -12.84368 | -52.94468 | 2025-09-10 04:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75c33144-1338-386c-9a90-70a0f1b21f68 | -11.94128 | -51.07981 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4ba41bf-302e-3187-ac6a-ed6884573cbf | -14.39275 | -47.32235 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e8dadb1-6057-3852-ac63-73aefc1bda5b | -12.04935 | -51.03927 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 81e51c7d-15da-30ca-945d-5a47db942910 | -16.67155 | -49.1399 | 2025-09-10 04:44:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b0fe4776-82e1-3c58-9f4b-efeb6c0c27cc | -16.39254 | -46.87562 | 2025-09-10 04:44:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61773237-f19b-3a15-ad2d-a419c4f55d73 | -14.57884 | -51.40422 | 2025-09-10 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c06ba6d6-ea5f-3f45-b3dc-8b7584e2e74c | -16.62622 | -51.82563 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a76d96a-3395-3ab3-8747-7e863c1a66af | -16.46885 | -50.6646 | 2025-09-10 04:44:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cd7e3bc2-799c-359e-a151-4c4e2c08f5cf | -14.88842 | -55.86998 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8654431-781b-3716-be19-94d8bc9dd422 | -12.84023 | -52.94408 | 2025-09-10 04:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1091168d-5f3e-3437-b31a-6c0fe80e3978 | -14.89907 | -50.12568 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e33cd2c6-3356-3a68-872b-5c42e98325b4 | -13.12392 | -54.92524 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 481251aa-eb8b-3b5b-a494-8ba1e96ea637 | -19.91789 | -46.1562 | 2025-09-10 04:44:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| caed9e86-107d-34c4-944e-026c5ebab96a | -15.02395 | -50.08475 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a0340d1c-e455-3018-b32c-00babba66727 | -15.8211 | -52.23094 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb0549fc-1cad-3f7d-83a6-276a790e44d4 | -13.22785 | -51.77099 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3ebd4a4-6072-32e6-b43b-bcaf0873d508 | -12.64599 | -55.95238 | 2025-09-10 04:44:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c354086-1cfd-3cac-beb7-f684f3114ae1 | -16.4597 | -51.97915 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b20615a7-f973-3bd2-9cb9-769263b4d368 | -12.01558 | -50.9938 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c7e75713-8350-39aa-9119-e7716d1def57 | -15.48052 | -49.3888 | 2025-09-10 04:44:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aeb18b2b-6810-39d3-a9f2-06abaa212e65 | -14.6042 | -43.92795 | 2025-09-10 04:44:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1d8c373-c387-322b-9a0b-7021119763d6 | -13.1361 | -47.15614 | 2025-09-10 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f93bd079-4493-308b-b034-9f30f5ce7da7 | -15.13498 | -52.3947 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1197cb4a-4bdd-3607-8982-6e8f1ac15b1e | -14.85874 | -49.53894 | 2025-09-10 04:44:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbeb244b-59f5-3f71-95c1-edd763b0d666 | -14.38705 | -47.33532 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a807484-dc7b-32e7-bcc6-c9cc0555f1d0 | -14.42567 | -52.95073 | 2025-09-10 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc233993-0e34-3cb2-8be2-0cee499a3728 | -13.94191 | -48.26088 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9398a97f-0f46-337b-8b8c-26a1ece21c69 | -12.93971 | -54.80546 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8941014-9d4f-38d7-8da8-3c0ee33f166b | -15.83446 | -48.96646 | 2025-09-10 04:44:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a17cce3b-2e9d-3560-90dc-186603b036aa | -12.86466 | -47.96526 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b50f5956-027d-3025-9544-841cf3815a36 | -14.38705 | -43.65088 | 2025-09-10 04:44:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94733d32-1b1d-3dd7-b732-4853d5226e08 | -16.83939 | -49.17174 | 2025-09-10 04:44:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2d34ab0-9cbc-3fb8-b2cd-169cbbd3df7b | -15.52396 | -48.3622 | 2025-09-10 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4afb72cb-5e3a-3742-a739-daa34ed7ed86 | -12.89557 | -47.97893 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9308b25a-86d8-3d61-95d7-7849e4c36f4f | -12.86407 | -47.96927 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 845f8e16-39b5-3dbc-8c93-c9a64798eec9 | -18.00686 | -47.11169 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f908c655-b542-3bd5-8fd7-6f440437c1d9 | -16.46099 | -50.67086 | 2025-09-10 04:44:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 42085077-7627-395c-b512-bfb9f1eb267f | -15.51831 | -52.76855 | 2025-09-10 04:44:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11f16b3d-97b7-3894-9322-3dd948a1ed9e | -16.46435 | -50.67141 | 2025-09-10 04:44:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8e68fcf7-be36-33d6-8b57-d3fbd04b6ca8 | -11.20737 | -54.98316 | 2025-09-10 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ba59d3cf-4542-358a-8819-b418aecf0f5e | -12.01778 | -51.00142 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f58fc605-3c86-3125-885e-6589fec98672 | -15.48512 | -49.38169 | 2025-09-10 04:44:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5713e253-6d1f-3636-b82e-7717c499afd3 | -18.4645 | -46.47647 | 2025-09-10 04:44:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a6ddbeb-52b4-354a-bab9-430e129296dd | -16.897 | -48.23212 | 2025-09-10 04:44:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 650d9c5b-2875-31fc-a4c4-b287ac9f6caa | -15.12059 | -47.026 | 2025-09-10 04:44:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bbf8fb7-c57b-3d7e-b841-90b2dd88610b | -19.81351 | -47.78821 | 2025-09-10 04:44:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76a473ac-73b3-37e3-90da-d7e9fe8e3c2c | -18.13297 | -51.72438 | 2025-09-10 04:44:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README80.md)
