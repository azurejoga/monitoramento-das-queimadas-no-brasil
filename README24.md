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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8373ba06-bab3-3e69-a629-3186cf1f7c4d | -5.7756 | -45.0826 | 2026-09-22 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 20b7a337-bb0a-3720-824d-c25ae1425de6 | -18.7472 | -46.93 | 2026-09-22 02:10:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 81.9 |
| ec035a7b-298e-39a4-9698-658331c3f4ec | -6.6516 | -59.9066 | 2026-09-22 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 1df6f0ed-4be5-3326-a016-908276722c7c | -3.2211 | -53.9623 | 2026-09-22 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 219.3 |
| 8aee7583-5144-325e-9574-2c518b362802 | -9.2383 | -46.1668 | 2026-09-22 02:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| b9cda724-7d61-3a6b-ba8a-9e6326a3658d | -6.6146 | -59.9272 | 2026-09-22 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 5b71cde1-f37c-388e-8e1d-c6d0402621d0 | -2.8608 | -57.7994 | 2026-09-22 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 73e392eb-76bc-307c-9fb1-7f2003bc7f55 | -10.5908 | -53.9713 | 2026-09-22 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 8e6a27b0-cbb9-31d9-9ba1-9731fd3d3d3c | -2.6852 | -54.9753 | 2026-09-22 02:10:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 9e5f1341-86c5-3ccc-8451-6e1b40ea6033 | -6.0925 | -57.6847 | 2026-09-22 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 2863ad80-611c-38f6-9616-426f5f911424 | -3.2395 | -53.9618 | 2026-09-22 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 198.4 |
| ab7e3491-a3d6-3270-9579-9740a3a93477 | -6.6331 | -59.9265 | 2026-09-22 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 9ebbf30e-152d-399f-8810-f7d40787ed5a | -10.5906 | -53.9918 | 2026-09-22 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 3188eaf2-6884-36ab-b31f-114973d054e4 | -5.7567 | -45.1067 | 2026-09-22 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| e0889913-bb01-347f-b733-449b29f8abbf | -10.6094 | -53.9902 | 2026-09-22 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 293.7 |
| 8ef57a75-955f-3fb1-96d5-960037709c1d | -5.7382 | -45.0853 | 2026-09-22 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| ee39b111-f2ab-3642-80e3-65498d373395 | -4.6668 | -43.5053 | 2026-09-22 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| d476350f-e8b6-3278-9745-2dbb76aa6ae4 | -11.3255 | -54.0487 | 2026-09-22 02:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| a89ff96c-3824-3b5e-bff4-18c2601046cd | -12.1458 | -47.3974 | 2026-09-22 02:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 5de17311-2d88-3d99-9784-eb72908e9711 | -11.3257 | -54.0282 | 2026-09-22 02:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| ca084a10-416c-35ab-bb27-cef59a5a65c4 | -6.6098 | -45.8991 | 2026-09-22 02:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 397429f2-7b08-3fdd-9ccb-29da6a719f39 | -6.6148 | -59.908 | 2026-09-22 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 6f00922d-bd62-3103-905c-8f002b534297 | -10.6283 | -53.9885 | 2026-09-22 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| a3de27cb-ed3a-3819-85e4-44eeed772d6d | -17.4416 | -39.9559 | 2026-09-22 02:10:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| 54c01d66-3da9-322e-a1e7-1a39010bda85 | -12.5547 | -45.9605 | 2026-09-22 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 59107bac-c8ea-3ab3-8712-40596a3f8686 | -8.7916 | -44.2778 | 2026-09-22 02:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ef1c6298-cbe6-3b01-9a0d-02503bcdc0c9 | -7.5889 | -57.6757 | 2026-09-22 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 96aead3e-58f2-34ae-8dc3-13063fdee39b | -2.6669 | -54.9558 | 2026-09-22 02:10:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| d8e97dd3-cb67-3191-8f34-50fda18eb000 | -2.6853 | -54.9554 | 2026-09-22 02:10:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| b6da34a9-abad-355c-88c4-a5a48eed054a | -6.61 | -45.8767 | 2026-09-22 02:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 87dbfaea-73e4-3642-9ef9-6571e42a7c27 | -12.1462 | -47.3751 | 2026-09-22 02:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 4a9565ed-2c97-311b-b8ee-05e829bf12ec | -6.6515 | -59.9258 | 2026-09-22 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 171.4 |
| e1b83ddb-00f3-3f5e-b1f7-71fbc44d9d3e | -9.2386 | -46.1443 | 2026-09-22 02:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 4e8cc54b-b62d-37ec-8d53-f56e66ecab80 | -2.6669 | -54.9757 | 2026-09-22 02:10:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 210e86d6-fe61-3861-a0f8-c551450e74aa | -6.0365 | -57.8235 | 2026-09-22 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 32a0656d-2cd7-3823-847c-c0afecfc7891 | -7.7144 | -61.2419 | 2026-09-22 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 32.8 |
| fbdd1cba-0197-3bfc-8b39-c124fc38de56 | -9.5594 | -66.0359 | 2026-09-22 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 362b3ee2-c550-3831-a6b3-52bef8aa2e8e | -7.5704 | -57.6766 | 2026-09-22 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| feb2f3d3-336c-3fc1-af78-87c2c127bcc9 | -5.7569 | -45.084 | 2026-09-22 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 2088f639-959c-352e-af75-fb27a950c4a5 | -6.0549 | -57.8227 | 2026-09-22 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 4e831d63-cac1-31c4-8c31-5508bd47e69e | -3.2396 | -53.9417 | 2026-09-22 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 256.1 |
| 208a9700-e1fa-386e-a6b6-30f20513b044 | -9.2573 | -46.1647 | 2026-09-22 02:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 1f92af0b-bd47-3681-bd14-d64db27d0524 | -3.2212 | -53.9422 | 2026-09-22 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 287.5 |
| 7aa58821-e767-31c0-9709-b867c17c562d | -6.6332 | -59.9073 | 2026-09-22 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| ff748034-52f4-3047-9f6c-bd5a1cc4a843 | -12.574 | -45.9576 | 2026-09-22 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 3df316de-12b2-3e28-986c-d6ae7950e098 | -6.0928 | -57.6262 | 2026-09-22 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 9940455c-1e40-3638-a737-13f32c241158 | -6.467 | -59.9902 | 2026-09-22 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| fbbbaf92-053d-3d4d-99ff-e0aacc667848 | -9.22 | -46.16 | 2026-09-22 02:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc738ce5-2441-3534-9160-7962946ccaaf | -3.23 | -53.94 | 2026-09-22 02:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afe60ef6-4e75-380f-8b99-a14b895ca19c | -10.59 | -53.98 | 2026-09-22 02:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 644a87e9-24d2-3c8c-a1f7-c9d519b6e94d | -5.76 | -45.09 | 2026-09-22 02:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 948e48be-99b6-3b82-b593-51629a7ae21d | -5.7382 | -45.0853 | 2026-09-22 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| f988ea99-ce61-3043-9df9-268946365dfd | -12.574 | -45.9576 | 2026-09-22 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| cf20e2e0-4593-30ad-a2a9-8e4f9538953b | -5.7567 | -45.1067 | 2026-09-22 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 2b415fab-8923-361e-b934-3f0342a56c3b | -10.5906 | -53.9918 | 2026-09-22 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 366dcbaa-22e6-3500-bd2e-ff33f8c8b67f | -12.5547 | -45.9605 | 2026-09-22 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 95cafa9c-c7ee-3678-86ef-3b9dc39fbd23 | -2.8608 | -57.7994 | 2026-09-22 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| bd0bfee4-5f59-30e8-979f-9f07176b5bee | -6.6148 | -59.908 | 2026-09-22 02:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| b68793fa-bcc7-3469-ac97-96727682d03f | -9.2383 | -46.1668 | 2026-09-22 02:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| afbeed7e-cde6-36f4-98f5-54d44ddaa2b2 | -9.2573 | -46.1647 | 2026-09-22 02:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 956890b0-c736-3cdb-a854-b50ab376fc52 | -11.3255 | -54.0487 | 2026-09-22 02:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 89413cba-6250-332b-95ca-9ff351b21869 | -6.6332 | -59.9073 | 2026-09-22 02:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 609db03b-9df6-3165-a5e8-590f69812d7f | -7.5889 | -57.6757 | 2026-09-22 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 5296719f-f702-3fc5-83d2-66fa06f94a06 | -12.1462 | -47.3751 | 2026-09-22 02:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 946ee525-aa49-3c04-b320-ded38b974623 | -6.0549 | -57.8227 | 2026-09-22 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e88ba974-b181-3993-92f6-3ae48d657583 | -5.7569 | -45.084 | 2026-09-22 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 9b87441b-3df4-3125-b0c7-0a607fd1c2ed | -3.2211 | -53.9623 | 2026-09-22 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 281.9 |
| da06d219-4981-37c8-8088-e243163cd08c | -6.6516 | -59.9066 | 2026-09-22 02:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 88c7a81b-26cf-35f1-acbe-3d2aa7b04f57 | -17.4618 | -39.9504 | 2026-09-22 02:20:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 87.8 |
| 541322fe-e38b-3c05-b969-a71dd427b05b | -11.3257 | -54.0282 | 2026-09-22 02:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 15d614f7-f806-3f5b-93a9-3602d9c15c10 | -12.1458 | -47.3974 | 2026-09-22 02:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 5036438e-94e6-30cf-99e0-6de8e7e75f41 | -10.6097 | -53.9697 | 2026-09-22 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.6 |
| cc835b82-94b0-3369-99f4-7db31acc740d | -9.2386 | -46.1443 | 2026-09-22 02:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| c8d6c1bd-b462-33ab-a24e-cb01200ff8ad | -6.467 | -59.9902 | 2026-09-22 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| c50224aa-596d-30f3-ad15-d339ff3ebb2f | -7.7144 | -61.2419 | 2026-09-22 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| fb4ad88a-6850-351d-8cbf-0ee1fe9ef7ee | -2.6669 | -54.9558 | 2026-09-22 02:20:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| b45db6bb-63d4-3ed5-9e84-96c235db9ad6 | -6.6331 | -59.9265 | 2026-09-22 02:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 176.2 |
| 738b8a89-8a21-3fe1-b3e1-bd5e1f57ecc8 | -3.2212 | -53.9422 | 2026-09-22 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 309.7 |
| 3b7fadee-67ca-35ca-ba9c-e910f43dff85 | -7.5704 | -57.6766 | 2026-09-22 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 7a6a6413-d2bb-3f81-8cd1-52813480cf23 | -8.7916 | -44.2778 | 2026-09-22 02:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 41be7083-405b-3a72-a998-bd6e9abebbe3 | -6.6515 | -59.9258 | 2026-09-22 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 173.6 |
| 173be3a4-72e3-3e3a-9d3e-e27e7a9e07be | -3.2395 | -53.9618 | 2026-09-22 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 333.3 |
| 29f0982d-beb7-3d9e-a9f8-cb1cc3b2d527 | -3.2396 | -53.9417 | 2026-09-22 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 344.1 |
| 057251be-17df-3c1f-9733-3e6b9a280d44 | -10.6094 | -53.9902 | 2026-09-22 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 263.5 |
| 8d83d74e-0d7f-39d0-b49f-44df78d79d3b | -17.4416 | -39.9559 | 2026-09-22 02:20:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 107.8 |
| 27aa6da3-d3be-3c82-9d74-5463f599324b | -10.6283 | -53.9885 | 2026-09-22 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| cdc5e931-75f2-3e84-906d-4f2a5ed11d79 | -18.7472 | -46.93 | 2026-09-22 02:20:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 2717f60b-54e8-397d-aadf-4711dc788d3b | -6.6146 | -59.9272 | 2026-09-22 02:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 135.9 |
| dfb83f14-e5aa-316c-a646-7607ce11a95f | -2.6669 | -54.9757 | 2026-09-22 02:20:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 9c7af661-63f0-3e82-9bd9-0e42333e1a88 | -6.0925 | -57.6847 | 2026-09-22 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 41f13ae6-4746-3c88-8234-c0b45b0f67da | -6.0928 | -57.6262 | 2026-09-22 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 566be93f-bcbf-35b6-9ccd-fe6cc4e459cf | -5.7569 | -45.084 | 2026-09-22 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 205.8 |
| 1fd2bc42-433b-3daa-bf58-11b3538ecffd | -10.6097 | -53.9697 | 2026-09-22 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| deb078da-eecb-3a0f-9f6c-4516f836ab94 | -11.3255 | -54.0487 | 2026-09-22 02:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| f3bf9f1a-5920-3b23-86a4-afaf21bcaafa | -10.6094 | -53.9902 | 2026-09-22 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 166.9 |
| db57b2a3-295a-3ea0-ac71-e28ee0e56e4f | -12.5547 | -45.9605 | 2026-09-22 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 4d44900b-f0b5-396e-9a09-fce1a800e21b | -9.4769 | -40.3365 | 2026-09-22 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 297.4 |
| 7020e782-0bd3-3eb4-ae0f-f983e6fbc7d5 | -12.1458 | -47.3974 | 2026-09-22 02:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 41941ea0-123b-399f-8cf2-1b6ccf1f82e7 | -6.0365 | -57.8235 | 2026-09-22 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| e526ac7d-2353-34fa-8b5e-dfa83e3af37b | -8.7916 | -44.2778 | 2026-09-22 02:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |


[Clique aqui para ver as próximas entradas](README25.md)
