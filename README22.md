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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11770b41-8a11-33b8-9228-f86d9e5895ad | -11.35125 | -43.56074 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 054c5d55-bff4-3d8d-b771-1dc8b04c8c2f | -11.32488 | -43.56046 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8e35bdb-e101-3ccb-a5d9-63de082a918a | -11.35329 | -43.55051 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b19b53f5-a202-3146-b2aa-597c336ddffd | -7.04095 | -44.38417 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| cabcdb89-5f3a-3e7e-9414-61de69a5b50a | -7.04848 | -44.36008 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39c4bc96-919d-3a6e-931d-a810daf8885a | -11.30049 | -43.55032 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0961d47-0eee-3f6f-a15e-6b2d8d18c80f | -5.78752 | -42.57102 | 2025-08-29 03:25:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 920862ff-db3a-34a2-a828-1a8f6cd59b6f | -9.85868 | -44.68901 | 2025-08-29 03:25:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7627023b-ca2d-32b2-82bd-bade6ba7b84f | -5.79217 | -42.60693 | 2025-08-29 03:25:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6a4d43b7-caa6-3c1f-a31b-1ac128e93095 | -9.86468 | -44.68472 | 2025-08-29 03:25:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0d134ed-dfb5-3839-b680-5bda580f4bf1 | -6.49219 | -43.53034 | 2025-08-29 03:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34970569-e430-38fc-8a32-8c2aa7774c10 | -6.8756 | -43.60466 | 2025-08-29 03:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2426a213-da61-3d5e-ad3f-312f90642e7c | -11.35011 | -43.57175 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fe5d3ea9-7bf3-3edb-b3df-de300c443ce4 | -11.34796 | -43.55016 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 777c7380-a25d-33a4-ada8-464e9b6525b3 | -6.44423 | -44.58292 | 2025-08-29 03:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db59631b-352f-3c88-8734-5db6692c6e88 | -7.63489 | -42.66637 | 2025-08-29 03:25:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8f8fd183-2a5b-3430-a15a-66405325567d | -11.50618 | -41.52253 | 2025-08-29 03:25:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ba431b4b-a4e3-37f3-b3d7-80a7b2547811 | -9.50782 | -45.38383 | 2025-08-29 03:25:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67f46e62-a1ab-3b5a-aad0-a7e5059ad024 | -8.43631 | -43.65585 | 2025-08-29 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3de710a1-e1ce-3e83-9793-305fddc63cad | -6.44565 | -44.57535 | 2025-08-29 03:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2832c394-b031-35e1-bfa1-8c9e0adfee67 | -6.26986 | -43.8129 | 2025-08-29 03:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41208213-367c-3e23-8984-edcf57b94b29 | -7.15166 | -39.42368 | 2025-08-29 03:25:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cad0402b-13e8-3df4-9348-16a60009b20f | -11.05778 | -44.76971 | 2025-08-29 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc23762c-3e6a-398f-9e2f-f11a2ab898b5 | -11.34799 | -43.54404 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72156cb7-189e-3211-a462-2fb0dd9e53dc | -7.04309 | -44.38775 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7c37a24f-4b71-3849-81c9-7375f17fb7ef | -11.34293 | -43.56933 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dd396505-1bd9-3cbe-aaf8-73988d2e39cd | -11.34696 | -43.54919 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcfd6f4b-a30c-34a9-8e89-97d3bd187464 | -6.08594 | -43.99718 | 2025-08-29 03:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d076a9a6-cad6-3d34-9afa-b90ab91d1a85 | -6.49248 | -43.53151 | 2025-08-29 03:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 60437df7-3e90-312c-9a3b-7ef966096d72 | -6.88106 | -43.6113 | 2025-08-29 03:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42f2bccf-cf01-39ab-a561-248be67a22a8 | -7.40593 | -43.38523 | 2025-08-29 03:25:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37fb41e0-c9a3-3feb-b98e-503a5d3d1cc9 | -7.42676 | -42.06451 | 2025-08-29 03:25:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 560c1254-d00c-30a6-9806-93c52a9535e3 | -6.4911 | -43.53612 | 2025-08-29 03:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b926ce51-7db1-37b5-951e-8d07c2f01509 | -11.12612 | -45.11941 | 2025-08-29 03:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc630928-3b35-38cb-bddd-82b81db54ab3 | -11.33477 | -43.28436 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 226b6e75-f21a-3dae-b849-6832d84d34f4 | -7.05179 | -44.3658 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db856c21-61a0-3f9c-837f-ca5b57097469 | -6.5522 | -43.93038 | 2025-08-29 03:25:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d8727a96-f93c-3c36-a83b-1f65113fe0c0 | -6.8708 | -43.63063 | 2025-08-29 03:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7bdb1b78-6128-32bc-85c1-def045eb4cb2 | -6.88126 | -43.61242 | 2025-08-29 03:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0990f1f-20a7-3658-8f49-19bdc0bebd05 | -6.88669 | -43.61898 | 2025-08-29 03:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f63d7848-4843-3d1b-a063-1bff2805a560 | -11.35758 | -43.56214 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d878909b-adce-3cd5-b0dc-e0498fbd7a16 | -8.45015 | -43.71537 | 2025-08-29 03:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c7075ab-ba57-3f08-8d73-0cd3b0fe17a3 | -11.29414 | -43.54905 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7146c97-ab30-366e-b899-973c022fa453 | -7.0568 | -44.3553 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f91d059-294c-322c-b2d3-6ec1ac281310 | -6.48695 | -44.40212 | 2025-08-29 03:25:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdff9c6d-9dc1-3427-a983-53a607a60ad4 | -11.03193 | -45.06965 | 2025-08-29 03:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b2f3ea6d-9eaf-3f95-8979-4a80e27186e2 | -6.87886 | -43.6254 | 2025-08-29 03:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c5f90b6-370f-3ffe-993c-77dd03068e99 | -7.04876 | -44.39668 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| dd900283-1a40-3085-b8b1-4cc9cea8db67 | -11.3438 | -43.57027 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2d11dc62-aa08-310e-b00f-fc5ffc10c20a | -9.50066 | -45.38194 | 2025-08-29 03:25:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 050c34a8-bf74-3357-9929-dcdb8b1fc9d1 | -7.41264 | -43.38644 | 2025-08-29 03:25:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a7587b0-602b-3c06-8204-b630aab02215 | -6.08497 | -44.00236 | 2025-08-29 03:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90739fd4-1722-3531-998b-4a3c40dea1d5 | -4.58616 | -43.31881 | 2025-08-29 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d077b41-bfb0-3836-8186-1b56ce92a1c8 | -7.05502 | -44.38801 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b65816e1-b0b8-3a7f-b53f-19b9ba6ce3d9 | -11.29518 | -43.5439 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08b68d37-a4a3-37f5-96a7-bac6688792c1 | -11.02984 | -45.06799 | 2025-08-29 03:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c16a23f2-1527-37cf-931c-49d7db96fed3 | -11.12038 | -45.12112 | 2025-08-29 03:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ab6ce799-7e6d-378c-a790-e3f502e5c937 | -11.35219 | -43.56168 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0ac9a2f2-5e30-3674-bcf8-e8fa7c9a28a4 | -5.79196 | -42.57147 | 2025-08-29 03:25:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eeb3685c-9bcd-34eb-8d4a-0c4983f7f30d | -7.42145 | -42.05862 | 2025-08-29 03:25:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e9fad094-bf42-3fd2-bd0d-277833da10e3 | -6.21738 | -43.33407 | 2025-08-29 03:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e65efe2-91ea-36c4-962f-c4d63f52ac75 | -7.05143 | -44.38293 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b5b357ef-846f-38d2-837f-d60884584ad0 | -6.53776 | -43.10395 | 2025-08-29 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21bfe69c-7934-3049-819f-24e19ac535ba | -11.30153 | -43.54518 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9deb2f15-bef5-3900-a0e0-8dbbc0af2fb9 | -6.53831 | -43.92702 | 2025-08-29 03:25:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f470df4a-60e6-3e48-8263-e21efdeaabfa | -7.04666 | -44.39313 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b66e9b6b-f5ee-3014-a5c1-e5df237afeeb | -11.34902 | -43.54503 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e3cd4a3-a80a-3129-9d74-cace6bcc45ae | -5.78805 | -42.60602 | 2025-08-29 03:25:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 20e1233d-95ef-330f-a604-26e2772b9afd | -7.05367 | -44.39519 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7554da3-cf2a-393b-850b-92823002c47e | -4.51566 | -43.69017 | 2025-08-29 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a23630c9-2b35-35a9-a158-0819d2c6d4fd | -7.62398 | -42.72427 | 2025-08-29 03:25:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2cf344ed-9e16-373c-a0ce-e08254177dea | -7.04576 | -44.37405 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 24100021-4c97-3715-b7e7-d9cef6f5ae78 | -6.48561 | -44.40903 | 2025-08-29 03:25:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40d5a47b-7a69-3e60-ad73-5fd3db4d76f5 | -11.30684 | -43.55159 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 687ba4b5-2ed2-3997-9579-385f5b3751a3 | -11.33021 | -43.56681 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38bbfed0-0461-3f66-9535-023a61a9adb5 | -11.28778 | -43.54777 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3192690c-1f19-35f3-bf55-bc0d971dcb8b | -7.04006 | -44.36538 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c9e1889a-a137-36d4-84e3-b1429a45a3e7 | -7.15218 | -39.42079 | 2025-08-29 03:25:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b2b997b1-9485-33c7-af19-68fef5a699d5 | -11.32916 | -43.57205 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 454d5787-f713-3e02-b8a3-f73c73916e52 | -6.54659 | -43.92161 | 2025-08-29 03:25:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 50743d28-e597-3847-96f8-a371abe0fd1e | -11.32712 | -43.58224 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de833a60-2eea-356d-b2f3-4c6183088127 | -11.31954 | -43.55415 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c022f81-0539-3738-8ae6-f6e8fcdfaf4b | -7.04981 | -44.35324 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75fd8b80-2d57-3bf4-805a-3d959c8e65c0 | -6.53964 | -43.91996 | 2025-08-29 03:25:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 8b69b868-5d56-3311-9248-adb79dbd2ef3 | -4.50696 | -43.68377 | 2025-08-29 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf6cfaa0-8984-34d7-bded-dcf70595d5e4 | -5.79425 | -42.57119 | 2025-08-29 03:25:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4bc7b927-1822-3db3-bd3d-a7f24536f92a | -7.0527 | -44.37637 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 65da857b-4c0d-394b-bcb4-eb69defb2202 | -5.86754 | -42.96346 | 2025-08-29 03:25:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| f3e2439d-0a58-3c52-84cf-6b2e4a7a2ad6 | -9.59641 | -40.35797 | 2025-08-29 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 99ef98c1-59bd-3c80-b163-6677244f8f8f | -6.7243 | -43.57791 | 2025-08-29 03:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96054f9b-f07c-35eb-9368-dabd6f6d5782 | -6.43969 | -44.56703 | 2025-08-29 03:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| da1255c9-5e33-33ab-87b4-928eec3d1a59 | -6.87048 | -43.62949 | 2025-08-29 03:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4aaa659e-aaef-3a9c-9a1b-813d0bf1582c | -11.35324 | -43.55661 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dcd822ee-bb1d-3691-9251-a849def3915e | -6.26872 | -43.81907 | 2025-08-29 03:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c66d0b5a-f0b8-3350-b416-18d6561ef5bb | -7.04487 | -44.36332 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ab7bfd0-6f33-38e8-9572-4266b60b353b | -6.54382 | -43.93634 | 2025-08-29 03:25:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 4898a894-b3ad-339f-adc0-ff774f18b099 | -11.32076 | -43.58095 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4cfa96c3-1e0d-37c3-b3c0-a46a53cf489b | -6.88232 | -43.60475 | 2025-08-29 03:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e32264cb-5516-3e5f-aed7-90fb682d55c4 | -11.05914 | -44.76312 | 2025-08-29 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc331ec5-a664-3c5b-a737-4a9bd8f4b359 | -7.05012 | -44.38968 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |


[Clique aqui para ver as próximas entradas](README23.md)
