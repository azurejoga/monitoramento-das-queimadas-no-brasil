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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ef2432d-4b40-3027-b2cb-0a9dd2f6a07d | -4.92394 | -43.18478 | 2025-09-01 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c3f8b89b-6505-3a12-aa70-fe8e4699065e | -7.0948 | -44.3358 | 2025-09-01 04:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 80a0e1ef-fb55-3bec-a6f2-204f959754bb | -6.8281 | -52.8143 | 2025-09-01 04:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| f80b87bc-edd5-3c3c-ae46-53feed42fb6b | -6.7626 | -43.7881 | 2025-09-01 04:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 2cd634bb-4313-31d6-9689-d2b6d3f5aff2 | -7.6783 | -61.0908 | 2025-09-01 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| c20be13e-87e0-3c29-a7f0-2cd9d109660e | -7.076 | -44.3376 | 2025-09-01 04:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| da8d42b0-2e92-35a3-8364-25dc09481f8d | -9.135 | -65.5453 | 2025-09-01 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a6492ea4-431a-3482-b91a-4b5cba1ce2e3 | -7.0946 | -44.3589 | 2025-09-01 04:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| f4e871fc-4f1a-3c89-8af3-38b2fdc1ec34 | -7.0757 | -44.3606 | 2025-09-01 04:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| b7155236-f7e1-395a-9283-4fbc0f037726 | -6.8466 | -52.8132 | 2025-09-01 04:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 26edaedd-c86d-36ce-aa63-b719f6a83cf4 | -6.74361 | -43.78397 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7d2ded17-f294-3ebb-ae71-7a6a3bcccddc | -5.40273 | -43.3641 | 2025-09-01 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22030481-324d-3c8a-97fb-e8698ae9767a | -11.37753 | -43.63255 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66e6fad5-ffea-3ac1-b599-bccb9fad028a | -6.18463 | -43.31551 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 235ce728-f249-329f-b098-3a1146db8671 | -7.40087 | -47.43651 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccd55068-4c9b-331c-9473-a84ecf964e6d | -9.64085 | -47.8098 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17994572-cdd3-3f27-851f-deef5105714c | -5.43984 | -42.91101 | 2025-09-01 04:10:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 14b984aa-a9d3-3382-9743-351152d624f7 | -10.76947 | -48.83117 | 2025-09-01 04:10:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53507a78-2e8f-3cc8-98a6-5f81e900878a | -9.21989 | -47.10625 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f77f6172-6018-3763-bba7-2301d18722a3 | -6.75881 | -43.7785 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ba0d5e21-9389-307c-9cd4-c2523a67849e | -6.45576 | -43.95382 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd5ffa58-48e2-38c6-bc2c-63d9642664a1 | -9.2192 | -47.11031 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 055a3163-7d98-3a20-ae03-8333935e1b54 | -7.88564 | -47.00205 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 849fe12e-6e7d-3c70-8aa8-01edee9002a3 | -6.8257 | -52.81476 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1e5cc108-0556-3db8-9bb5-e7a965306ac4 | -6.4903 | -44.07162 | 2025-09-01 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8eb7d7f6-49ea-3a30-955e-edc9e8acca5a | -9.23169 | -47.08632 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3483062c-3d55-3771-8083-0dcd4867e963 | -6.23632 | -43.38901 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f06e3294-6a5d-3462-9bb0-507fed0a9b68 | -6.14958 | -44.14621 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44834c44-ade6-3928-aae8-75c974a0dcaf | -6.46486 | -42.42378 | 2025-09-01 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d0b33220-22a6-36d0-a3d2-748febb903c9 | -12.31078 | -45.68044 | 2025-09-01 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb952fd6-9ef1-3d77-b898-7429e098fb14 | -7.08365 | -44.34773 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 9957e9d1-d729-3106-b049-c3b853225799 | -6.16101 | -43.33922 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20c22926-f820-3bd7-8abd-fa51445fbcba | -6.37015 | -43.54924 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9457d35c-a3e6-3b27-8448-f4ee5715ec88 | -9.925 | -51.62305 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95116ba2-686f-349c-b701-180c0850cac1 | -7.61498 | -42.65774 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7c8172a6-7329-349b-8f70-4ac4d97f69a3 | -7.85408 | -45.23621 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd66fc0d-7a3a-36cb-a5db-15fe30da9e71 | -8.83593 | -47.51638 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57918e77-8b96-3fdc-8ac2-69cd9204d35f | -6.93177 | -42.0197 | 2025-09-01 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c32faceb-8311-3a36-b1a6-649117bc2564 | -6.26291 | -43.54407 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db8f9f13-de43-37ea-be93-344748c6103c | -6.3051 | -43.61311 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c3a9bd46-6be0-32f5-bfa9-83bf21ddbd7a | -6.3674 | -44.45138 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29f107e4-c0cc-378e-8c84-06d9da50bd29 | -5.85858 | -42.93555 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cdbaca2b-52a9-3d74-a3f5-bfdea9b11955 | -11.04619 | -46.96467 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 019ca89b-7327-3ca2-b005-1ead9cbf5ca3 | -6.33717 | -53.42785 | 2025-09-01 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6c85b60-6ff3-33b6-9869-84a8c7535abf | -6.55036 | -44.08137 | 2025-09-01 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d35355e9-ea7d-3f26-8f89-e7f3b149dd6b | -6.84857 | -52.82617 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb5962ca-ca30-3c6a-b069-8f68a55036e3 | -11.78985 | -46.43829 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b7b2be4-0240-3e53-a820-a4657dd0591e | -11.48881 | -46.81692 | 2025-09-01 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0676e1d2-761c-3c91-9f89-6db04fc4d6bb | -11.96138 | -45.80264 | 2025-09-01 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a8ac592-dc2c-3640-88ef-3d84635aecd7 | -8.19944 | -46.76882 | 2025-09-01 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 17827187-8b95-3256-9ee8-75cf19181166 | -6.18726 | -43.34271 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c7fae07-d1d5-3057-8421-fab364494e72 | -11.87479 | -46.73691 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b475be7a-0192-3eca-99d2-360d0e4e9336 | -7.08787 | -44.34431 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 7f0f1eae-e6e4-372f-9729-1c17dd451e71 | -10.24171 | -51.11741 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d2235778-40bc-3250-a377-be22989491eb | -6.27987 | -43.52723 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8081517d-54b4-3dd6-a472-c2eba989d51d | -9.63726 | -46.60168 | 2025-09-01 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c80a052a-4652-3b26-b4dd-9ee7d5c9a73f | -7.24707 | -44.06057 | 2025-09-01 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d0f6948-0e61-3bc7-a38b-cbddee2ea902 | -7.58582 | -42.68941 | 2025-09-01 04:10:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4523ae31-98ae-3ff4-9370-8f544fb86db3 | -6.742 | -43.78874 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f7665ced-37ea-3748-a62b-24e147bb488a | -11.79062 | -46.43377 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9efe849c-a223-32a6-9cee-b7eccddf0403 | -6.58461 | -43.71563 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe6eb3c5-13dc-31e0-8b7c-7d9fcd0567a8 | -7.09007 | -44.35303 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9e5bc5f9-0ccf-3da2-a2bb-675ba6a58526 | -7.98185 | -46.43534 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa054e11-8c22-3b2d-91db-7713fa5f89d7 | -10.03071 | -48.05755 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5226c1bc-55df-327c-be91-402e103f33e1 | -7.07493 | -44.3429 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10eaf3fd-cb39-3c04-9648-b8549926897e | -7.69263 | -46.71844 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85e4244c-3a51-3bb2-9269-a3c48028b40c | -7.2467 | -44.23806 | 2025-09-01 04:10:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f4b025c-15e6-3c9d-84a0-0e4d56e5a942 | -7.69903 | -45.00122 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac27942b-27b9-3390-9417-aeda644c5d75 | -6.33425 | -42.54061 | 2025-09-01 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 08396631-f4ca-3c1d-9811-81c04e6dc1ff | -7.10737 | -44.31467 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f612d8f-8ea7-34ec-adf7-493f5ffaa416 | -6.84117 | -43.33945 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 15a8a5fb-7304-3337-8502-c50ba0576af4 | -5.80107 | -42.55503 | 2025-09-01 04:10:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a1172c77-5158-34e2-bd73-62c2d8ed830f | -7.62999 | -44.03367 | 2025-09-01 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ab1b1acd-d294-3d00-bd46-00421ec8eca7 | -9.1445 | -45.20192 | 2025-09-01 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b70e3eab-b90a-3dfc-84b6-39d12672ab87 | -6.50901 | -43.55932 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9263f11f-6bcb-380b-ad87-0e22bb5d92cc | -8.84828 | -47.49489 | 2025-09-01 04:10:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59b1ab99-d6d1-3e32-aa34-85f09f6f262e | -6.74262 | -43.78489 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a17ba393-516e-3c85-ad97-34e535c96bfc | -7.97794 | -46.43452 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8ea7c1e-7bcd-3a11-84db-762f80893bd3 | -7.00275 | -44.35984 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3aabbec-9818-3a56-ba2d-ab364554b683 | -5.81692 | -43.21664 | 2025-09-01 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b6156b8-e084-3eb4-9297-a7c2652cf317 | -7.98679 | -44.05808 | 2025-09-01 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bd3387f-bc87-34e0-b2e3-c913321de7aa | -6.79532 | -52.80633 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 32e32395-95d3-3f14-bdb9-00ec78821207 | -6.18179 | -43.31124 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76ab71bf-efdc-3eed-9bdf-ca9355a61095 | -5.88395 | -44.32306 | 2025-09-01 04:10:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d60f4ab-9be2-31c4-a289-d07d88952e9e | -6.30044 | -43.29212 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f3b20fa-5b42-3fe3-a897-476cf9f04c67 | -6.82409 | -52.8217 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7a3e0f7f-7dfe-3f2f-ad2a-d59ab25d56bf | -6.29977 | -43.62408 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52795fd5-e8e5-3fe6-b853-1856c9f3c0c3 | -10.79046 | -47.26425 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7a27f2e-f1ab-377a-b145-deb31b7bb112 | -11.08907 | -44.73736 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99feb47d-e142-305d-87c1-fb3aad676186 | -7.11157 | -44.31133 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 85f92e14-c5d7-3537-b128-19dcdbd10609 | -7.07072 | -44.34631 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b01e3e7b-5263-319e-b273-3abc13548a04 | -6.02944 | -43.77967 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fa65383-2e2c-3684-b36b-ece2c111272d | -6.45201 | -43.69072 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3edcc7a0-0eac-3bc1-8313-81bf23b3013f | -6.16505 | -43.33603 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe998922-ab37-30b5-975b-ac0064154d8d | -9.26581 | -47.12902 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5903d52f-3342-33f0-bc43-0d30caacabc9 | -5.11611 | -43.22586 | 2025-09-01 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e3aa4c9-597e-3a36-9c4d-77c859d12189 | -6.82843 | -52.83245 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7e194f48-14bf-3168-83a7-b383e9ac5256 | -5.6543 | -43.66628 | 2025-09-01 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eee761d1-d2d8-314c-bb05-d0ef65bbd6ad | -9.38073 | -48.01705 | 2025-09-01 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af36296e-87a7-3a4c-837c-bd56b61da9ea | -6.74931 | -43.79277 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README27.md)
