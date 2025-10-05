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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa2ae1b5-c3d7-3041-a023-4db88b2c509c | -12.58959 | -48.14003 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 615840e1-92a4-3754-ae41-c0a33578895b | -15.22597 | -49.28814 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| aed7b0cc-b08d-388e-9ea7-c37374896098 | -13.33325 | -47.7875 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2337823-e9bc-388d-ad14-df0dfa1e8193 | -13.35295 | -48.06345 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8d8952c6-9057-3b03-89df-db6296c9ad7c | -11.95219 | -51.47796 | 2025-10-05 05:16:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64b97997-8f9e-39dd-b01f-9d3ae77dd5a7 | -12.81698 | -50.53794 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f8a7ac49-6c11-3358-99f3-e742a4b1bd4d | -13.57746 | -48.15739 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8d52f1f-7b16-3240-a643-9a1750cc27f9 | -12.59063 | -48.13141 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b96eb318-ef1d-36cb-b051-0a98e49bf022 | -14.33089 | -47.67843 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| af9b61d9-22d9-3f88-846b-95748d0aa5ad | -16.01608 | -50.95585 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4aa501d7-c09b-3ee2-ac31-5a20c3c00dde | -15.21771 | -56.85384 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a02e9aa-3e0b-3619-a78c-6619be342c48 | -15.55002 | -46.82231 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d02af58-7db8-3996-9c85-ab95b753a269 | -15.99202 | -50.91884 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b8b5bd9-4034-3192-9056-a8b1bceb32e7 | -13.28237 | -47.58621 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 140801a1-1b3d-3f01-b466-c82eb57acc1f | -17.89561 | -57.64195 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| eb3d76cc-66bb-3f78-8b8f-86763c59db08 | -14.33286 | -47.69939 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c7c71e1-63df-31e3-9638-d35be1569518 | -14.67757 | -48.3615 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 35b28fac-596c-3e67-b452-07ee0e01a7e5 | -17.32815 | -54.20122 | 2025-10-05 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 404ef932-da93-33aa-acf4-783b3a11b33b | -14.59215 | -52.46283 | 2025-10-05 05:16:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a07cd3c8-1283-32f9-b4ab-745719442f31 | -15.98257 | -50.91075 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| afb6c753-1935-3258-9e65-687680f80d56 | -18.25193 | -53.33338 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2c9fb7b8-6a85-3e54-99a1-26d2b30a8af1 | -13.08532 | -47.89652 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c71e8726-efd8-3617-9b0b-e6fb365a3d39 | -13.26166 | -47.81783 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6005a3de-2084-3a05-b7e1-fec69e1ae4f2 | -13.36212 | -48.06509 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 55c3efcf-4e82-3cd9-b822-e54109011431 | -17.85346 | -57.63298 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 80c9dafb-322f-3dc5-a87b-37029a3a3f72 | -17.7131 | -56.7454 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d6f80f03-ce30-3a8a-990c-d6f565aae859 | -13.57697 | -48.16168 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 432a262c-6337-3692-a7ca-b926e1797b59 | -13.15269 | -47.96817 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9f157d0-9a1f-3a1f-98fa-8b37f91ab639 | -18.18957 | -53.35684 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5b5972e4-4fe4-3c97-8460-7be618493ff6 | -15.57043 | -52.47443 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e033418d-97bc-3a32-b529-b9bed00d766d | -12.31893 | -55.1384 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c47eed7-42f5-32c1-8838-39a940b35213 | -10.99696 | -57.04745 | 2025-10-05 05:16:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7d492db-c7fc-32f6-ad40-7213e0ea2ab5 | -13.26749 | -47.60702 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ed95134-2cf2-3bb2-a9a4-43d84883b981 | -13.54795 | -47.23728 | 2025-10-05 05:16:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b23e67fa-2105-38de-b13c-653c4b6cd08e | -12.98674 | -51.01123 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb989e9e-ae30-394b-94e8-3cc517d4eaa7 | -17.87154 | -57.63195 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 860251f5-2012-3f2d-a0b6-e12cbb71e9df | -12.26759 | -55.12598 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfbbe8a9-feba-3c19-b99a-747e0d32f420 | -12.23585 | -60.33565 | 2025-10-05 05:16:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12c329eb-0826-3f14-9c87-4241d88f8d5b | -12.9225 | -47.30278 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dbf95672-b428-36dc-9657-c237d6624a2c | -13.48256 | -47.2872 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9ba071d2-6a35-3a30-84bb-e212ba972758 | -14.60858 | -48.12422 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09e2b8c8-adb2-340c-a226-0d292fdf3a01 | -11.84901 | -63.71938 | 2025-10-05 05:16:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d91e2643-634b-34f2-a85b-000184d86b9c | -13.26119 | -47.8219 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ed0ede44-21f5-3beb-b2d2-ab58c422738e | -15.21184 | -56.84598 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d353b4fa-a7d6-3cb3-88cd-d0adb24110df | -13.25213 | -47.20641 | 2025-10-05 05:16:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5b800cd5-4b65-33f5-b4ee-20a195b3cc19 | -17.94998 | -57.58833 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 93ee4f44-03b0-327f-aa62-b0fc9e9103b0 | -15.36164 | -47.98311 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0932380c-61af-3891-8e8b-9089fe5ecee3 | -14.58822 | -52.45746 | 2025-10-05 05:16:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e742c4b4-b439-3e51-bc8e-fc72951fd8db | -14.68926 | -48.3651 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 186eaffe-0a73-36ab-b611-bae5fdc61479 | -14.68487 | -48.29267 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fde7f9d7-0dd2-30b4-b942-8cfaeb8ab495 | -15.30128 | -59.23748 | 2025-10-05 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4a72e9e-6c52-3291-ac0d-f2f4d78108a1 | -17.70282 | -56.76835 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d4b4c0b7-ca03-34cd-9305-d9989fc71415 | -11.84498 | -63.71866 | 2025-10-05 05:16:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14e16798-fb65-3e91-8278-455b83e6d88e | -11.94591 | -63.17082 | 2025-10-05 05:16:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9af8b907-7472-351b-9c0c-d5ce353a3af7 | -12.41375 | -51.10752 | 2025-10-05 05:16:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3c5d3380-a129-3838-83e3-2f9b42bc236f | -14.87903 | -48.2618 | 2025-10-05 05:16:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31547f2c-5537-307a-850c-46afba14df8d | -14.68042 | -48.36986 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 203b8d95-b3d9-328a-84c7-36d54bfdd94d | -16.08314 | -50.91733 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce4e5a71-2003-32f8-aa6f-70360a561fec | -18.17995 | -53.36085 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8584bc1d-f318-3391-a6ac-b96205a2835b | -14.62119 | -48.12127 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dc3932b-6d9f-36e2-be64-7badf0e6e909 | -17.94766 | -57.60438 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 4a53a31d-a0f8-37bb-a6ec-c4265e9ac83d | -15.37301 | -47.98146 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e85fdd7-63aa-367b-862d-655c18d96d0e | -14.32538 | -47.67158 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c05dd08b-b559-3d18-95e3-24d65af23cb2 | -16.12697 | -53.9834 | 2025-10-05 05:16:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52aae582-309c-3eac-8cc9-4023b5357514 | -12.27066 | -55.131 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e2f1c2d-66b6-3880-87b1-2d86c9f0e677 | -13.12892 | -47.94185 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b3ce2cde-8a2e-3527-b4b6-9ab47577e385 | -13.35892 | -48.06427 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1cf88ff2-ef90-30e3-9199-c8dbac5fec46 | -17.70885 | -56.74922 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2fe4fe50-e625-3b22-86a1-2663b4156f25 | -14.67437 | -48.36993 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9c40f2b9-17c7-38ed-971a-a13eda17ce10 | -17.95351 | -57.58878 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 885917b1-116e-31f7-af1b-5073f169434e | -10.83889 | -57.18771 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f9f879c-8f17-3d2a-8f09-1c2f30fb143b | -14.855 | -60.06485 | 2025-10-05 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64a227a4-e0e9-32e9-a16e-bf3f6de91c92 | -14.33014 | -47.66553 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7a486a07-b50f-35c1-9853-09fde3a992c9 | -10.84068 | -57.1839 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 721b5f6f-b6fb-360b-8f6e-8de775d08765 | -17.88389 | -57.59653 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9a6a5470-cd19-3f7e-84ab-5207467e39bb | -15.3029 | -46.30695 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1273f6b8-0c54-3c49-b2e2-0f744b924a35 | -13.46309 | -47.29045 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 881e8198-7e4d-3878-83fe-f41c32a2c1de | -15.75142 | -46.27362 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53f8c61d-835c-30ed-91a3-cfcc1bfea3e6 | -13.73414 | -47.9684 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff3197b2-e26d-33d8-973d-4b8585e89a51 | -14.66883 | -48.36556 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2f29fbf7-0333-3922-b02e-f473ce5389cb | -18.24008 | -53.35499 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86f6b748-c6dc-35ee-9ebb-e385ff316834 | -13.72717 | -48.08372 | 2025-10-05 05:16:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 02a24dee-3428-32ce-85ae-507c41509376 | -12.2713 | -55.12656 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b6e6d77-585e-327d-bef5-ee28412e9ffa | -13.27873 | -47.61766 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40daa874-4e2a-3ac3-b0c5-a79ce5aa5893 | -10.65347 | -58.75519 | 2025-10-05 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96738782-f111-3936-b14f-0b3fd2d54830 | -11.00035 | -57.04799 | 2025-10-05 05:16:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75b707f2-0d4c-3a65-9e0d-ab6a2774a8ff | -14.95173 | -46.84496 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98182ab2-be1b-38af-a76d-2cb45537c427 | -17.95176 | -57.60086 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 2587d26c-92e4-3ace-8cb9-8ac287378825 | -13.36492 | -48.06484 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de2ba2f6-d2ef-36c7-b66b-c9fa09e9542a | -11.83052 | -60.48768 | 2025-10-05 05:16:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b235901f-0d58-37d3-9dc9-f5945e2bac67 | -17.8985 | -57.64376 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 579f4bfc-c1dd-3447-bfcb-e9dffa3df205 | -14.82726 | -54.76457 | 2025-10-05 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78dc6e55-e2cb-3228-996f-18d27d79ca30 | -15.70244 | -46.27883 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13b1c16e-1997-3a6e-b9cd-cebc63af3517 | -18.24453 | -53.35594 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95fc980b-e950-3eb5-ab58-295d40a56ee8 | -11.87264 | -56.88108 | 2025-10-05 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f5d20f24-d8d0-3662-914e-89b0583bcf9e | -13.14428 | -47.96663 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 114d8c3e-dead-395f-b40e-c7f2ff34fd5d | -14.33417 | -52.96923 | 2025-10-05 05:16:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e5922e8-4139-3e0c-978d-ee20e08595d7 | -17.96876 | -57.58277 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| fc979ad8-df0d-3529-8d40-c5417d3d168b | -15.23076 | -49.29626 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ce2dc3e-5457-3c89-9a19-344f7739d3f5 | -12.30891 | -55.15499 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README140.md)
