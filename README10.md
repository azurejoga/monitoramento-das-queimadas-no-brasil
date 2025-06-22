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
| fe694d41-056f-3d51-80ba-56c14a9d1fef | -11.46941 | -41.43335 | 2025-06-22 04:42:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b23a9462-a560-3471-825b-a04a7f8a388d | -13.23882 | -49.83994 | 2025-06-22 04:42:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c80e84ec-3a79-3654-a7f3-cf02384cf088 | -10.0265 | -54.32438 | 2025-06-22 04:42:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04515428-dee0-3b45-b726-ebb6333dd7a6 | -14.49327 | -46.98771 | 2025-06-22 04:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3a13dee-e2fc-3aba-b925-73d01ce1ec65 | -8.30756 | -55.09969 | 2025-06-22 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5198d7bf-f18a-36ec-8fd6-25a20edbd398 | -13.75032 | -47.75 | 2025-06-22 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bad3820-a5e9-3917-8866-e0030c5ccc6b | -10.89108 | -56.4615 | 2025-06-22 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6122f7d3-342a-36eb-b5e6-c9c3b4a7ee47 | -13.04488 | -53.71244 | 2025-06-22 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9f3509d-6673-3238-973f-2f6a2c6f3c0c | -9.92219 | -59.91219 | 2025-06-22 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fef608f5-ab43-3bf3-a420-e3161bc7d8e1 | -9.09803 | -50.02542 | 2025-06-22 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b9a61a7-0ecc-376e-bff2-3eeca0a721dd | -12.26988 | -54.53484 | 2025-06-22 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 110fff38-e92e-351f-a199-8cf82deb6482 | -11.95365 | -58.76577 | 2025-06-22 04:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e79e7cc1-d7c5-3cb3-9b94-67a54c12f7bc | -10.0609 | -49.66386 | 2025-06-22 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bbdd3e5-085e-3fcd-852f-40d3017431e7 | -10.43168 | -51.82978 | 2025-06-22 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e57d4c42-f27e-3b7f-a6a2-f8b100b47546 | -11.57225 | -52.0986 | 2025-06-22 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 801011c2-5ffe-3318-9cee-50782bbe6700 | -10.0259 | -54.32165 | 2025-06-22 04:42:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1558c00-366c-32ed-bb5e-7e776d81c45f | -12.52339 | -57.24053 | 2025-06-22 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f1e4463-9bf2-3f2e-8786-c49b8769f72d | -14.02382 | -53.36752 | 2025-06-22 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ef828177-3e2e-3ff1-b4ae-b9fd07b82ec4 | -11.78793 | -57.23862 | 2025-06-22 04:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 722ef832-c40e-3a32-8a83-479d6b1d04ca | -12.02612 | -57.09921 | 2025-06-22 04:42:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97545407-d8d8-3c32-992f-2ff54700b522 | -11.10114 | -46.67432 | 2025-06-22 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53de80f4-e902-31d3-86e3-6c3d2a0a2bbc | -9.32827 | -47.82695 | 2025-06-22 04:42:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f3e85ca-459a-33ed-87cb-7b52812df753 | -9.25635 | -57.52462 | 2025-06-22 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0036337f-47f5-3638-9c1d-ced8c5e9d5e0 | -8.60165 | -51.5863 | 2025-06-22 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3d3a6a83-1871-3214-9732-16fdbb1f0e4e | -8.5644 | -51.5577 | 2025-06-22 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba318a39-b472-3e0c-8682-cd3941ae804e | -10.98536 | -45.09206 | 2025-06-22 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ed0e360f-988a-34e1-a252-e3b46bbc59af | -9.25543 | -57.52964 | 2025-06-22 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5b77dd9-ecba-3715-9c02-e988245cda6a | -11.84586 | -57.76264 | 2025-06-22 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5f6b656-c958-36a6-8ebf-6884b2d228dc | -10.88609 | -56.46472 | 2025-06-22 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7b0d21e7-6169-35c6-be32-8cd8979804f5 | -13.79962 | -54.29191 | 2025-06-22 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 32ff8573-7ba2-3962-b95b-4c82b01e8642 | -9.91673 | -59.91109 | 2025-06-22 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4fb03db2-3c8c-3f8f-bd46-95d223135ca3 | -10.56747 | -46.93597 | 2025-06-22 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52b29d93-6e7d-3151-8c0b-87afefa7265f | -12.50271 | -58.35506 | 2025-06-22 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 054cdf95-4a77-338d-99d9-133ccf5e842c | -13.78811 | -54.29415 | 2025-06-22 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 691c7f39-327d-3c1e-97e2-bb37028a9652 | -12.57588 | -56.9723 | 2025-06-22 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da4c3489-cd01-3db6-ab28-65bc437b233c | -8.59824 | -51.58578 | 2025-06-22 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0b2276af-f806-3265-94dc-78dfd6016acf | -12.30147 | -50.08667 | 2025-06-22 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9b5922d-39d0-3e5d-bb06-ac3b77fb55c3 | -9.25543 | -57.52691 | 2025-06-22 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cc026a2-7686-307a-a90f-244721d05e20 | -10.86291 | -53.7603 | 2025-06-22 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 054249db-e738-3548-b1a2-18b8ca174fb1 | -9.45589 | -56.0626 | 2025-06-22 04:42:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e13f09ac-ec1e-33e6-9967-6642204cbc5a | -12.02772 | -57.09056 | 2025-06-22 04:42:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a312e1f-0847-3ed8-91da-11fdfbf13249 | -9.16895 | -61.40641 | 2025-06-22 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7a29ab3c-0d8c-3474-9b03-fd2050583754 | -14.25891 | -45.50656 | 2025-06-22 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02082416-3c43-3ac9-8245-e5d3c269588b | -12.57661 | -56.96822 | 2025-06-22 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7078dec-0749-37f5-9240-13c67a84a474 | -11.61097 | -58.29056 | 2025-06-22 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8ce9f4bb-1271-3bf3-9934-abfe2561f521 | -9.46835 | -57.84453 | 2025-06-22 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db20079f-f3d2-37c9-9ce2-eeb24fa4d1cb | -11.8785 | -54.67051 | 2025-06-22 04:42:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe126b0a-f818-3ed1-8543-839a69a05ea1 | -14.25945 | -45.50254 | 2025-06-22 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fd2f647-e16d-3052-8d9f-196f9d5ebe30 | -9.14933 | -47.14996 | 2025-06-22 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edf3822f-a26e-366a-a76b-effe8a20c141 | -10.88964 | -56.46954 | 2025-06-22 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7982ba66-57aa-356f-9ab1-e3cb908cfd38 | -10.52072 | -53.61919 | 2025-06-22 04:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c288af34-6608-3250-94e5-6f61e7f5626b | -12.1324 | -58.17958 | 2025-06-22 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b2b3248-2155-304f-b49d-adfc077b5db1 | -11.87474 | -54.66983 | 2025-06-22 04:42:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3bbce56-b0c3-358f-8d4b-0eb14bb2f2ef | -10.98122 | -45.09142 | 2025-06-22 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab1d1710-1bc8-3871-86be-33625c72d64c | -10.06922 | -49.65432 | 2025-06-22 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02f1d511-f2ed-355e-93b9-868d3c68f658 | -13.0378 | -53.71118 | 2025-06-22 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14fb8801-46c2-35f8-b16f-69c27c2f7e90 | -12.41711 | -43.81498 | 2025-06-22 04:42:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 753af1bf-a13d-3df2-bf0b-3b9ba675a939 | -10.22877 | -54.29302 | 2025-06-22 04:42:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3471cc02-cd33-397b-a00e-5673f1259811 | -11.78392 | -57.24334 | 2025-06-22 04:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 823269d2-38e5-3cbc-91af-951f09ac94e3 | -8.59883 | -51.58212 | 2025-06-22 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c4efa2f8-c732-3a2d-8f3b-6296d03cef0f | -13.8054 | -54.3016 | 2025-06-22 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2270d2af-0133-3ff9-aad6-fc0400da6a8a | -11.42532 | -54.32936 | 2025-06-22 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cd02b75-6125-3bdb-b4a3-8dc5a7426f69 | -10.06588 | -49.65379 | 2025-06-22 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff308e04-3b31-3c85-9c26-eef9dd75627f | -11.56827 | -52.1017 | 2025-06-22 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b6c3a4b-8bd3-35c8-bb7f-0abe299ba6a8 | -10.98589 | -45.08828 | 2025-06-22 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 16848a33-b056-33dd-847d-7b7240459b56 | -10.89391 | -56.47033 | 2025-06-22 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e732149e-b756-3ad4-a1a3-93dd3a2eb409 | -10.02969 | -54.32231 | 2025-06-22 04:42:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6d72cf9-01d0-3aa9-9180-e18c05461a31 | -9.14872 | -47.15409 | 2025-06-22 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3fd752d8-1955-34fd-88aa-4d37410c8585 | -10.03028 | -54.32507 | 2025-06-22 04:42:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a9dd754-9832-31d5-b3ec-a7d28938ac4c | -10.8196 | -54.04263 | 2025-06-22 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e28608ab-53c0-3802-b6fc-0ee2df1dfb45 | -11.56946 | -52.09437 | 2025-06-22 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 22d11518-65bc-3330-bed3-558006d8a3f4 | -10.05756 | -49.66333 | 2025-06-22 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e660a4dc-5a93-3a80-a82c-53af8747156a | -10.51036 | -47.57811 | 2025-06-22 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35686196-4bd2-3213-b671-f4d2da8c49dd | -10.95758 | -49.572 | 2025-06-22 04:42:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a935ef9-7c95-3d3d-a9a0-cac87a69a826 | -9.45945 | -56.06737 | 2025-06-22 04:42:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2d081b21-d518-3b1c-a81a-32b68de33101 | -10.06423 | -49.66439 | 2025-06-22 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffd96a62-f30b-34cb-8ec5-64d7ba55da4e | -9.46442 | -56.06406 | 2025-06-22 04:42:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3d874e18-3980-33a4-a8e4-873526d37afb | -10.60322 | -52.84008 | 2025-06-22 04:42:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85739d8d-e105-3178-a01e-ae811dd3156d | -13.7874 | -54.29834 | 2025-06-22 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0c640daa-6909-390f-a8fe-014edbc974ed | -10.52726 | -53.62466 | 2025-06-22 04:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5526f73-de5d-3444-b705-9951d7fe89e8 | -13.791 | -54.299 | 2025-06-22 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9d426098-6a2d-37e3-bd6c-7962a331dc24 | -12.13148 | -58.18457 | 2025-06-22 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 025b26cf-e4f8-357e-b048-457492f5d8d4 | -10.85928 | -53.75965 | 2025-06-22 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec9bbd98-d432-3841-acd8-f823eb458e8d | -11.74297 | -54.71549 | 2025-06-22 04:42:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7a2c94cc-2d54-3536-b87d-b1fbfc0b9c16 | -10.50976 | -47.58216 | 2025-06-22 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b8f51b2-4343-3c0c-b0e3-bd3103289856 | -9.25451 | -57.53467 | 2025-06-22 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0a6a79d-8a03-3008-86fc-211bd994b72f | -13.49529 | -53.49991 | 2025-06-22 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54c633b7-1f99-318f-a6d7-b1d5a9c2d67e | -10.52797 | -53.62043 | 2025-06-22 04:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84b21431-b192-3770-8642-7180bab108d1 | -11.73335 | -49.05986 | 2025-06-22 04:42:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2004e7f2-65a0-3929-ab1f-7df42ae6edf3 | -10.86732 | -53.77875 | 2025-06-22 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c76f7f3-549e-3924-90d7-99fe81e5c374 | -11.79234 | -57.23949 | 2025-06-22 04:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c60a210b-0b40-3ea1-b957-783c2f399d02 | -14.25468 | -45.50599 | 2025-06-22 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8eda69d-7982-38b2-88f8-eb5a0c6a5efb | -9.4566 | -56.05855 | 2025-06-22 04:42:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 370dde9c-d910-3b5a-9426-153496f20a9e | -10.52293 | -53.62826 | 2025-06-22 04:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| af1e2601-1a67-3d1c-b32b-f1c4d961f399 | -11.36343 | -55.12598 | 2025-06-22 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53395195-1fcf-3ebe-b194-66f60a26859c | -13.23602 | -49.83576 | 2025-06-22 04:42:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fe8dff7-830e-36f3-9aea-0bf5f08f8255 | -10.59647 | -46.91795 | 2025-06-22 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b8b9333-79dd-33a4-b54f-a088649f95f3 | -11.42608 | -54.32486 | 2025-06-22 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ff5fdc1-b642-30bd-a88c-f77c774e4183 | -10.05866 | -49.65627 | 2025-06-22 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4ecd705-fed4-3513-b8fe-a64ff4e366cd | -10.95422 | -49.57146 | 2025-06-22 04:42:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README11.md)
