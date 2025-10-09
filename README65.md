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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f43014db-0666-357a-9baf-00a854cd0a7a | -11.99442 | -46.7676 | 2025-10-09 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ed653f00-34aa-3161-92c9-e06625fb8cec | -17.21968 | -47.66077 | 2025-10-09 12:19:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3988efa3-23bf-31e7-ab91-7813da75e408 | -13.37907 | -47.20691 | 2025-10-09 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8ca17d2f-fd8a-36f5-91fd-cf2f7243b931 | -16.29455 | -47.13752 | 2025-10-09 12:19:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ddab8077-66bc-39a7-945e-2be3ad73557d | -13.82821 | -45.84829 | 2025-10-09 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 8afa955a-160f-3a85-ac80-68f27e22367e | -10.22735 | -46.09459 | 2025-10-09 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| f9cb5041-088f-37b5-9d6a-494a776256e1 | -10.43314 | -46.60149 | 2025-10-09 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6f4c04b2-c0ab-3604-a889-5f731b5883b9 | -16.68417 | -47.59533 | 2025-10-09 12:19:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 207d46c4-b243-3cc7-8cfd-d83768f07f7a | -13.83113 | -45.82603 | 2025-10-09 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 0319745c-7d37-36fe-9e48-87d857414368 | -13.32405 | -43.59156 | 2025-10-09 12:19:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 937317cc-4f64-3f58-b655-ed313404c408 | -14.25495 | -45.86817 | 2025-10-09 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 5d4b8c1a-1365-30bc-86e4-89706848dced | -13.42894 | -47.57677 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 399cbb39-aba2-313c-88d0-433843341e1f | -13.42242 | -47.62337 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 160.1 |
| a207867e-20fb-3a3b-b46b-b33378056518 | -15.00902 | -47.53862 | 2025-10-09 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| b66b2489-b1f5-3af9-aa84-f19498ad2f24 | -16.69335 | -47.59671 | 2025-10-09 12:19:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 879fe54b-5800-3792-98c4-09c7f36ce353 | -13.02438 | -47.89773 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0bde350d-0969-301f-a82e-a7c0ac710d49 | -12.22776 | -50.94836 | 2025-10-09 12:19:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f5d3c16a-1204-3da6-8dca-62be14379eaa | -14.84806 | -48.43148 | 2025-10-09 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 425c03af-7523-344b-887a-d0cd6808bab2 | -13.37 | -47.20557 | 2025-10-09 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8cf10d5c-f051-3e63-a552-b021de96dc4c | -15.39126 | -47.29917 | 2025-10-09 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8447061b-7b7f-3511-8a5c-caa71a652954 | -13.43903 | -47.63519 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 256.5 |
| 67869f3e-0863-33b1-aaba-9b1417ddfaae | -11.50071 | -47.65715 | 2025-10-09 12:19:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7dca30c1-adaf-3d58-a077-3418f846eeed | -13.43008 | -47.63387 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 92a0451d-de1d-3b62-965f-66247d7fb199 | -14.53194 | -48.71032 | 2025-10-09 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| bb7b6939-1f6f-30ef-9b54-d7368da58020 | -13.24741 | -47.62271 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| aa8610cd-5fca-345e-b109-87b717b2c78c | -11.7234 | -44.30148 | 2025-10-09 12:19:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 39.7 |
| e96d8500-45eb-35e1-a528-79b39e2d8455 | -14.40783 | -46.0092 | 2025-10-09 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 2dcbb159-8bfb-3ebe-ba3f-d12d5c1dfbb7 | -10.83506 | -47.08616 | 2025-10-09 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 32dfc1d2-026b-3f01-9a7d-493f8e32a4b2 | -12.95426 | -42.47704 | 2025-10-09 12:19:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 74.4 |
| f4e63de1-a1e7-364c-8a16-d1efc9cb2dd5 | -14.4049 | -46.03112 | 2025-10-09 12:19:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9b1016a4-b4b7-396c-8309-dbf25f2800f8 | -15.55895 | -45.31535 | 2025-10-09 12:19:00 | TERRA_M-T | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| c03a5c63-295e-358f-ba94-11a5658b01b2 | -12.22617 | -50.95893 | 2025-10-09 12:19:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c4a35be9-6c92-30a7-89b9-a4b299757a20 | -18.05356 | -44.9503 | 2025-10-09 12:19:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 27b3afde-af71-3740-99b2-27505afc9cc6 | -13.05679 | -47.93626 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1985ed72-8e97-3307-8b17-6f4a4278de05 | -12.28594 | -47.64897 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 37e05ad4-c6a5-36d7-9ffb-9c97b0a12820 | -15.96956 | -49.09742 | 2025-10-09 12:19:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d197db30-cf6b-367c-b33c-0868696a3ee6 | -11.77969 | -45.04976 | 2025-10-09 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| d2c07df5-aa88-331b-9d44-0881cb4a256f | -13.80722 | -45.85699 | 2025-10-09 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 14be75e9-19de-3702-a3e7-a3e215969dbb | -13.83404 | -45.80378 | 2025-10-09 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 2d2c2358-50c0-39e9-bccf-21d89ddf167d | -13.40467 | -47.554 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 16d62604-44ae-3024-937d-34bff2d0fbb2 | -10.87319 | -47.98825 | 2025-10-09 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f7032f7d-e009-3a89-a799-dd43c6da6617 | -15.78873 | -50.27451 | 2025-10-09 12:19:00 | TERRA_M-T | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 156a8fa5-64f3-3c8f-a7fc-693449a414a8 | -13.42114 | -47.63258 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 374c40dd-71ac-356a-9d13-d9fda1eeca81 | -12.26147 | -47.88663 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.2 |
| d824efbf-b92d-31f9-ac0b-09f434cc819e | -16.70386 | -47.58815 | 2025-10-09 12:19:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 28816d2a-d0a8-3fb7-a89f-39fac5534503 | -13.44161 | -47.61673 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 261.7 |
| 81ab5ff7-8905-3e93-a947-31fa9ceb9a3d | -13.79456 | -45.87813 | 2025-10-09 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 2473e251-7cbe-3a58-b827-74104ba88940 | -12.69617 | -47.67613 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 8f34ad3e-f5fc-3931-b9de-8e27abb4d308 | -14.38842 | -46.00617 | 2025-10-09 12:19:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ef26cfa4-90e8-37e7-8030-cc99348f6121 | -15.75442 | -48.99707 | 2025-10-09 12:19:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 247b9e77-b01c-3d66-942c-9d0f01d22e0f | -14.72761 | -48.36383 | 2025-10-09 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d3c29eaf-fa58-36dc-ac22-c66c01bdc988 | -15.49447 | -47.9562 | 2025-10-09 12:19:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7777b53f-a602-3682-99fd-b682572472e6 | -13.77105 | -45.81167 | 2025-10-09 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| aa64d829-d81b-3291-a89c-7e890b539c99 | -11.53464 | -47.09266 | 2025-10-09 12:19:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2ad5d51f-859c-363f-9f9a-211a81674cc6 | -12.4148 | -45.71635 | 2025-10-09 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| c3c51d95-240c-3b21-af2a-5020d675e35a | -15.75572 | -48.98796 | 2025-10-09 12:19:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bea80762-64ab-31ad-98c0-358b407f5a64 | -13.81013 | -45.83451 | 2025-10-09 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 224cdc3f-22f4-3530-89bb-6a96d8111ca7 | -14.51772 | -47.29015 | 2025-10-09 12:19:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f1a9c8b6-f89a-3c7e-8acf-dd7598453bec | -10.23659 | -46.09585 | 2025-10-09 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 18461a94-7260-3777-b023-e0946b17e9f1 | -13.79746 | -45.85571 | 2025-10-09 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 05e52498-f01a-3a19-b8d7-dde5d28314a6 | -13.77255 | -45.80038 | 2025-10-09 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 04634ddf-29cb-3429-a450-b7cfac38f769 | -13.4288 | -47.64305 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 31.4 |
| d2817c69-3e27-31e1-a292-35d2d05a7cb9 | -13.40095 | -47.24911 | 2025-10-09 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 07206e53-236e-3a98-898c-4ad12f404035 | -13.30256 | -48.47082 | 2025-10-09 12:19:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 31c5cffe-60e9-376a-b766-19b84e46a03e | -16.06246 | -50.9717 | 2025-10-09 12:19:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e24e201f-0bfb-3d92-92ce-b21cc223f0b4 | -13.43398 | -47.60608 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 37.6 |
| fb7a46d1-8cfc-3023-98c5-fe8965f8e57c | -13.42372 | -47.61411 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 702770d8-eee3-3823-8614-07f8e4fa179b | -15.99404 | -50.81421 | 2025-10-09 12:19:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| dac2ecae-5e72-3e98-8816-d3b373f271da | -13.43774 | -47.64436 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 233.6 |
| f67d01b2-8620-3396-abab-e296ed24cb2b | -13.8365 | -45.86078 | 2025-10-09 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 052822d2-d0ba-3093-ad7f-3d0669565c78 | -15.39841 | -47.98444 | 2025-10-09 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 14a31c63-048b-3875-8e77-dffb96a9cdfd | -10.42892 | -44.99806 | 2025-10-09 12:19:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 21.4 |
| cf3ee42f-c139-319d-b1ec-e13dad31c78b | -15.39057 | -48.04081 | 2025-10-09 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ec93322f-b2c4-30f3-b856-5dec0062a578 | -15.40621 | -46.27349 | 2025-10-09 12:19:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ff811523-bca2-3183-b2c5-3741d7dbdadf | -16.28517 | -47.1365 | 2025-10-09 12:19:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 38f3c828-4913-33a9-9bdf-02d19dc44186 | -13.23975 | -47.6122 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0483541d-4e3a-38d2-b938-1591a1fcebcc | -11.1285 | -47.74475 | 2025-10-09 12:19:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 24e8972a-b85f-3ada-853f-4fb3e938ff3a | -13.79601 | -45.86691 | 2025-10-09 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 220.5 |
| 6dd05efd-44d4-3002-a7c7-f321a7a703d8 | -12.0674 | -45.73867 | 2025-10-09 12:19:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e21af949-a5e3-3b31-af51-30216906aec7 | -13.2859 | -48.0157 | 2025-10-09 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 114.2 |
| cca5681c-892f-387c-9171-1dfa8e075260 | -12.9509 | -42.4886 | 2025-10-09 12:20:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 138.0 |
| e4cadb00-cc6a-391c-a154-376a1d994e2a | -12.425 | -45.7056 | 2025-10-09 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 520ab35c-d8d4-314c-b799-62373b82ec73 | -11.993 | -45.1958 | 2025-10-09 12:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| e66c882b-33b4-3d6f-bd26-b412d1e7cec0 | -12.4438 | -45.7257 | 2025-10-09 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| cc088a0f-e417-34a1-8869-d1b54d16e1b6 | -11.7215 | -44.3084 | 2025-10-09 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 6414d347-b512-371e-b47a-c6f43feb9a36 | -17.6538 | -44.4339 | 2025-10-09 12:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 51fff17e-8e1f-3d01-a767-7b67e0a4f112 | -12.6964 | -47.6776 | 2025-10-09 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 197.2 |
| eed6c292-ac15-36c9-b2db-0dd9821e9ff7 | -17.6415 | -47.2103 | 2025-10-09 12:20:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 6bce632a-1499-31ad-9914-684233adde93 | -21.25606 | -51.66768 | 2025-10-09 12:21:00 | TERRA_M-T | SÃO JOÃO DO PAU D'ALHO | SÃO PAULO | Brasil | 3549300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 1e1960bd-4310-3aef-8f8c-be8c15f39ad1 | -17.91101 | -57.5129 | 2025-10-09 12:21:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.3 |
| ad1bfe9c-de0d-3dc4-8931-f40851a7006e | -23.15983 | -52.14187 | 2025-10-09 12:21:00 | TERRA_M-T | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 21c731b0-8764-396a-a485-94d2ca32c3b7 | -21.04589 | -55.57943 | 2025-10-09 12:21:00 | TERRA_M-T | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9b5e0788-7c8b-36b9-9609-f03e1fc33864 | -19.20907 | -51.591 | 2025-10-09 12:21:00 | TERRA_M-T | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 7b812391-3486-3ced-982c-157efb38d576 | -30.56891 | -52.69553 | 2025-10-09 12:23:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 4.8 |
| f6cb1d2d-3f5b-3d54-b4b1-f56aa94de82e | -28.97263 | -51.06671 | 2025-10-09 12:23:00 | TERRA_M-T | SÃO MARCOS | RIO GRANDE DO SUL | Brasil | 4319000 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2d911d45-98ca-3714-97db-71bcc292039d | -29.74997 | -51.57357 | 2025-10-09 12:23:00 | TERRA_M-T | MONTENEGRO | RIO GRANDE DO SUL | Brasil | 4312401 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| db119434-77eb-3c29-8e68-a4bfb7c6bc00 | -13.8108 | -45.8288 | 2025-10-09 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 214.6 |
| c4bd3d3c-d7db-31ac-8fc6-f788412052e2 | -17.6538 | -44.4339 | 2025-10-09 12:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 5b5b1602-66e9-3fd9-9eec-303dc99c1b61 | -8.6106 | -45.102 | 2025-10-09 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| c7401278-27ed-3257-bcc4-d11a1ec22130 | -13.8307 | -45.8024 | 2025-10-09 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |


[Clique aqui para ver as próximas entradas](README66.md)
