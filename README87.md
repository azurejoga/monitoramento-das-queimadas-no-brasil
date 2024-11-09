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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c61912f-84b5-3749-99e9-5e5dac65377b | -2.81339 | -52.95858 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c93d3b87-d8b9-3f88-8321-5c9ae9e3f980 | -1.32895 | -54.59969 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e13b0f04-75c7-39fb-9249-c9b606f616dd | -2.93395 | -52.53332 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4791ba13-14b9-3e53-9eb2-065d552c7344 | -3.35846 | -51.6416 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a1b7640-4a36-32fa-8741-4564bde559be | -4.3963 | -49.85247 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 430dc806-a883-3c9f-bf63-54118be35614 | -2.04223 | -52.654 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24a1e047-dc7f-3292-91f6-b3344ca562c5 | -3.70736 | -53.75243 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4ecdc287-fec8-385b-8861-03b7f6b59355 | -0.9062 | -51.76402 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45ae7827-9a29-3a59-bdaa-37f5e9c203df | -2.22177 | -46.54355 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a118b413-7442-39dd-ba51-98ba47d38112 | -2.84299 | -51.97057 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c45df64d-8612-3261-93e5-838c56813459 | -1.46442 | -54.97618 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0f3b6ef-55fb-375e-ac34-3e62bbc8dfed | -3.3862 | -54.68742 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 815862b4-ba11-3cc9-a9d9-8e9efc70e988 | -2.21257 | -53.72009 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46883a38-9ebc-3199-b06c-41a21e9979c1 | -2.86619 | -49.14775 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea1d298d-0379-3b22-aa1c-2efcba33adc0 | -2.88492 | -48.2965 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f4ff801-8124-3173-8bbe-e9dcaa4da8ca | -2.97865 | -50.30128 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8292bf05-eb29-324a-94d7-03de9f62bf12 | -0.22283 | -51.63662 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc8e4aa4-dd32-3703-a8c2-edbf8d2ee34f | -2.294 | -48.55602 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7522e491-485f-3ebd-a2ac-aa07cb000bb8 | -2.63527 | -51.71432 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5145bd5-fbe3-353a-ab7b-dee6d0497891 | -2.25637 | -53.72337 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec6b5cd2-52f1-3cb6-a9e2-0eb9de2b73d8 | -2.24205 | -53.77088 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 759fd4ab-dfdf-3461-8632-9c2c8cc53969 | -3.81813 | -50.79668 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02f5125a-cacd-3377-b658-ec34d31e4139 | -3.22793 | -53.24955 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ecde5dd-58c2-3d39-9767-28da1cb30220 | -3.04939 | -50.3786 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a439adc0-341c-38d7-a439-d305fccabf88 | -1.03339 | -53.73101 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dfd1d2c2-3170-3347-a761-965fa33a0c68 | -2.88088 | -49.37493 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31e5df65-7079-32c3-b8ef-bb887cf46dd5 | -1.3391 | -54.62358 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4db16da5-2df7-3d07-9de5-6ce1290340ea | -2.63266 | -46.0354 | 2024-11-09 04:55:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8e9c9f96-2be7-393c-985b-445780aa4750 | -3.63068 | -51.82023 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4d85eb4-dd87-3560-8866-8c5b25ff690b | -2.20783 | -51.94561 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90b50cba-7de4-3d6b-ad36-734d66fb3469 | -1.55529 | -52.26936 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f590cf4c-02fe-348b-a774-27d7e1f401d1 | -2.3906 | -46.78292 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41574f93-3294-3189-a125-7148b5c17d94 | -3.1015 | -53.70678 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb44e032-aa14-363c-8c12-4d4a5e2294f0 | -3.2699 | -46.31634 | 2024-11-09 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e1ea9664-7919-37e1-bb7c-f6c86cc605df | -2.88887 | -54.11432 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ce2ba58-4375-30e2-833e-309de3668a77 | -3.70476 | -51.38845 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80a5051e-bbe1-352c-aff8-0f6772a546ee | -3.5995 | -50.23707 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71db9202-433f-3d01-9865-277bfb0573e3 | -3.03579 | -48.04374 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a996270d-4aa4-3a6e-9a8c-47541b94589f | -3.23351 | -50.45517 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc4e03e2-1710-39c4-a15b-d6057703675f | -3.90081 | -51.92492 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d7f0a15e-5c47-3103-bd60-2ad792ef2f70 | -0.9034 | -51.75997 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc63a51c-24e9-3388-a5b6-099f1c58c101 | -1.41727 | -54.76782 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ac922b0-2396-38b0-88fe-087a17276fe2 | -2.88501 | -49.39884 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 209f0f90-0549-3822-88c5-ea5a69c50e19 | -1.1493 | -53.66027 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fa8506e5-59ce-3db0-a7b4-c952fa0f22e8 | -1.3831 | -52.19632 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7f42861-2deb-3421-8ecf-0f278d8d8ac9 | -2.21868 | -50.76515 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b27ec6c-3f96-3dc0-94dd-ad28931b69f5 | -3.17127 | -57.08667 | 2024-11-09 04:55:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc268825-58b3-329a-a04a-ad0dd3a88840 | -2.20772 | -50.74374 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc33fd4a-4ec7-3e6e-8bb3-a7973fe74797 | -3.20583 | -50.63213 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 52b760cb-7708-3d19-a4e0-74e1782f55a3 | -2.37086 | -49.35897 | 2024-11-09 04:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97fa6ee5-c12a-35f8-85f1-467c6385b1d2 | -3.72849 | -53.40229 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc1a4bf9-0bc8-3c4b-a0f2-4e249a805b1d | -3.42799 | -49.2466 | 2024-11-09 04:55:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e22b7cc-1d95-3e2f-999f-b4631945c0a9 | -2.29005 | -48.55542 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 376863b7-ac31-3c09-a5b7-c72aa8399ff9 | -4.31046 | -48.65495 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c96766f8-5cfd-3b87-bf5f-db7b1a261d06 | -2.461 | -53.69116 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 336e0354-ae71-3497-aa4b-78516dd87a6c | -2.15004 | -49.13784 | 2024-11-09 04:55:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26c7b796-dc48-31a9-8a45-5fd4e8582257 | -2.2251 | -46.43279 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ee8bd0c-d0b3-35bd-95e1-d7e458113fa3 | -3.76567 | -51.64922 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 518855e1-9968-3a35-a347-500a523b47d8 | -1.50938 | -47.1769 | 2024-11-09 04:55:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8509e81f-f0b0-30f6-bdf2-b85835290727 | -3.35713 | -50.26246 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c92e278f-aff3-3902-882c-79abf974256a | -2.06897 | -52.27028 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17d10cd5-9a9d-3e04-9b1a-28b082a20cee | -3.6298 | -50.18375 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 290f3873-3b46-3ac2-93fe-21a427d8ec77 | -1.38993 | -51.57215 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd4a33b0-1c2f-35f3-9d61-a4dcdae6bbc6 | -3.37155 | -51.64741 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 133094de-639b-35d4-b228-8f36732ae914 | -1.35286 | -51.40461 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 704bdfc2-487a-3be0-8ea0-17d341b5b36b | -3.23573 | -53.39218 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea3485ad-eb91-3bba-8553-930e678c9de7 | -3.03727 | -50.32712 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 18cda7e4-68a2-3ba7-aa43-344902e66423 | -5.68964 | -46.43438 | 2024-11-09 04:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 023087c2-cf2a-3454-a073-a6b09efb3181 | -2.41018 | -50.30495 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a82a3b6d-408b-3c75-97ad-ffa1b8c37f40 | -6.17907 | -45.44426 | 2024-11-09 04:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6c236880-c212-3801-a5ee-46af4ef2bbf9 | -3.96085 | -48.16753 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56b07a0b-683f-34f7-86a7-71e908b3d0e4 | -2.61951 | -51.74885 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63488ce1-bed7-3a4e-96ff-9d08fe643e06 | -3.83009 | -51.90695 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3e54e1d-dc3c-302d-8e7e-76eaa9121be3 | -1.37867 | -52.20277 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8344f9ab-7220-35d5-b6fa-655aa88e8254 | -1.30138 | -55.72577 | 2024-11-09 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e7fd6db-2d49-3f2c-afcb-91b29e9e855d | -2.93453 | -54.12201 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff4b5b38-de8f-3196-8611-24667ece54f2 | -2.46001 | -47.84159 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b46d658-d7a4-32e5-9d92-6e325f055e2e | -3.58878 | -47.35807 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f701556f-7b5a-3fd6-84be-97ee1e884748 | -2.91724 | -51.04772 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 284ba940-d61f-3ada-800d-9ddb3cec5528 | -2.83532 | -49.47236 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d761464-b50b-3d5b-8c06-14873b4e0582 | -3.45411 | -54.60705 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e40fb5f2-7819-3812-a987-9a0f2bea206e | -3.20252 | -54.58898 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6f69d35-1a09-3679-a4a0-860e7b92f48c | -2.92999 | -49.50765 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25453f8c-727e-3649-aa84-099e97844301 | -2.61235 | -51.74439 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a1ddec8-3498-37d2-ba1d-40369422be95 | -6.23421 | -47.28812 | 2024-11-09 04:55:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f8639037-7421-3240-a1b0-ccc19c27086f | -3.22582 | -53.28454 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f4c3b96-ab0e-3da1-bae7-059ea92134e4 | -2.05352 | -52.08472 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08a47d4e-250f-33ae-8b69-15afc5ec20ee | -3.69804 | -54.61937 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2798b74b-2848-3853-9578-ea5a30f69728 | -2.21304 | -50.7327 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62967526-41a3-35bf-be6d-bfba9b8472d1 | -3.40377 | -50.01044 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 67d98b8f-7dcc-3b6b-8e4e-6a59547a4ec4 | -3.91263 | -52.40408 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77e56baa-c13e-3cb5-8c82-8beb54ebe978 | -4.12611 | -43.59236 | 2024-11-09 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4a4f7a1-ccf1-3170-b788-aff9f246d389 | -2.92414 | -51.67341 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a72f43ea-f9b4-312c-9d08-fcccffd66f05 | -1.07688 | -53.17737 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7765eda-57dd-37ec-a74a-a5df61a9ba4a | -2.92471 | -51.66978 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f488c2c2-b3dc-35f8-ad02-543cc20b6f53 | -2.29476 | -48.55105 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2bbda01a-8d45-39ff-93f3-ad560cc3be2c | -3.23406 | -50.26207 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f7287dab-d633-3155-a1f0-db583caf98f3 | -2.92261 | -51.4593 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7558d249-740c-3a9b-af81-99dda3b2f3ae | -4.30472 | -46.27133 | 2024-11-09 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7473389-8a29-3195-8518-d77c61338651 | -2.21519 | -50.76461 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README88.md)
