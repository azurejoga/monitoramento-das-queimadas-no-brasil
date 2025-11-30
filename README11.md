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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9054cfbd-a4c6-391e-b971-1dd13b82440c | -3.42807 | -41.00709 | 2025-11-30 04:23:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0a6874a3-7c7a-3d15-965b-c2776c9d3a75 | -2.00816 | -46.41919 | 2025-11-30 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6fed5ab-0343-311f-a2bf-aa31de49f336 | -2.44505 | -47.08481 | 2025-11-30 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d38a92f5-75ac-306f-a110-298c6e53715d | -1.88365 | -47.92196 | 2025-11-30 04:23:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 48af38e5-b329-36aa-a286-9b9153d3db73 | -2.3234 | -45.85204 | 2025-11-30 04:23:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23addbb7-9b6e-352f-bbf9-b5c43cd1476b | -2.35065 | -48.61959 | 2025-11-30 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88350b45-acd8-3146-bed6-eb8431b98c36 | -8.17189 | -43.2045 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 4739488e-8374-3ba9-91d1-124d20f70422 | -2.35438 | -48.07501 | 2025-11-30 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dbd12e8-35a5-35c5-83df-4c244313a239 | -8.16731 | -43.21144 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 24f42ffd-bace-3679-89f7-dd92fcdef7e8 | -8.03726 | -43.13087 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c826af17-926a-3c20-8b4b-e26226b1db31 | -2.60522 | -47.34463 | 2025-11-30 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5e2d060-fb6d-3350-ba17-82edda577163 | 3.34955 | -51.33997 | 2025-11-30 04:23:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9afa66cb-71e9-32a9-ac5c-941c1609588c | -8.04069 | -43.1314 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e0264bcb-3290-3e2e-a29b-a881615a6312 | -2.4421 | -47.08004 | 2025-11-30 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1dd7a7c5-1a36-3f10-8720-77074d36001d | -2.25975 | -47.38411 | 2025-11-30 04:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cabb6bbe-c3c8-343f-a65e-6873af0dc764 | -1.88704 | -48.39968 | 2025-11-30 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 025e9dc3-3ca7-307a-a7e3-77f1b23f51a3 | -7.73403 | -44.18509 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52d4c06b-edcc-3b1e-ae34-4407c8f85814 | -3.66008 | -40.90282 | 2025-11-30 04:23:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ddb65093-76e8-3184-975a-9508990333e3 | -2.91313 | -40.38667 | 2025-11-30 04:23:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a4ef8227-3942-35ca-bd23-0643c8d42f75 | -9.29882 | -40.3667 | 2025-11-30 04:23:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 56ba9e10-c114-3346-bd6e-6aab14dfef6a | -7.45714 | -44.74251 | 2025-11-30 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5ab03c91-e474-3110-bdd6-6f4ef50e51f4 | -2.31947 | -49.16621 | 2025-11-30 04:23:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b84f246-b961-3974-b668-d2d30de6abce | -8.04128 | -43.12765 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9194b7cb-919f-3a56-a6f5-c03ef60bab4e | -7.73737 | -44.18561 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 031d62c2-46d1-37ab-bd0c-80b5d616a3a6 | -2.97028 | -44.96992 | 2025-11-30 04:23:00 | NPP-375D | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 361a3277-f7a1-3005-b313-59a386f431cc | -2.76994 | -45.18198 | 2025-11-30 04:23:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f28f7c0c-369a-3e4c-a279-4c22b8052448 | -7.75018 | -44.19119 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf4ec9f8-35f9-34ee-98cd-532d40333e3a | -2.38619 | -47.61031 | 2025-11-30 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a253881a-ce8a-3101-b9e3-e62263817281 | -7.74071 | -44.18613 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07e14eb4-a19c-3048-9f48-2ff76efd5016 | -7.73458 | -44.18156 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95b43e7f-b359-30b5-88ef-9d554854866a | -7.32918 | -38.76344 | 2025-11-30 04:23:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0e4e885f-94c1-39ee-bbf8-8ee00edbd85d | -2.32164 | -49.16705 | 2025-11-30 04:23:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc59c788-89ca-3105-b439-922cb2fa0897 | -1.7954 | -48.06796 | 2025-11-30 04:23:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 277169b7-0816-39d6-ba83-9fba71824d77 | 3.35193 | -51.32002 | 2025-11-30 04:23:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a21d92a9-9ef1-3005-8e53-715e10743ab6 | -1.47488 | -47.75056 | 2025-11-30 04:23:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 980d5217-7fba-351c-9fd7-bc4389f5d352 | -2.54106 | -47.8 | 2025-11-30 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 537ad125-26e8-330a-b986-7d628b99fcc3 | -8.16102 | -43.20664 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 5f667670-ad3e-3c08-a72e-e51a6a60223f | -9.29478 | -40.3661 | 2025-11-30 04:23:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5878caf3-3a93-3f9e-b534-b0e27b042b81 | -2.44642 | -47.07642 | 2025-11-30 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9eb4bb32-2203-3354-9be3-e2dd35a9b228 | -3.2692 | -41.38254 | 2025-11-30 04:23:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d462a184-e7bc-3df6-ae46-11148091ff8c | -2.24474 | -46.51955 | 2025-11-30 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99dd71d8-c84b-357e-81c7-28fff65804fd | -8.16045 | -43.21038 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 7ba97a9e-ba00-3d0c-8984-388b5fe7cf8c | -2.63816 | -45.916 | 2025-11-30 04:23:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 629f6096-d6e6-32d7-a82e-fafbe9eb873e | 3.3524 | -51.32318 | 2025-11-30 04:23:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2f8353c-c7ed-3f66-8f54-3f54a614f2d3 | -2.20985 | -48.00554 | 2025-11-30 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4aba54e-9e0b-37d1-838a-b668e00c8cec | -7.46716 | -39.95989 | 2025-11-30 04:23:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 29d251dd-3ee3-3b3c-9e4f-cafbf24e54bf | -2.21063 | -48.00076 | 2025-11-30 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b36a6f8e-bfd3-3c98-b60f-8149ad52ba31 | -6.31471 | -43.8124 | 2025-11-30 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ffff603-d871-3ee0-91f4-e66c335d7bc6 | -2.00752 | -46.42316 | 2025-11-30 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29d6a8f5-b509-3428-a545-4414162303aa | -3.42326 | -41.01442 | 2025-11-30 04:23:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 91011ed2-8bc9-35fa-91f9-8abf330f452c | -2.47374 | -46.28455 | 2025-11-30 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 40732047-b356-37e7-b1f3-b2dd6611636f | -1.88288 | -47.92672 | 2025-11-30 04:23:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a5b6bbb4-1ac8-3bbe-b48a-8677a391ff95 | -6.8745 | -39.56584 | 2025-11-30 04:23:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dd57b096-c954-3ebc-a054-4789c648da69 | -6.30747 | -43.81488 | 2025-11-30 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 978c1028-698a-36f3-9d0c-5f976dac7c6c | 0.85443 | -50.18679 | 2025-11-30 04:23:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7b97f23-b579-33b6-a22b-51b983ab9d38 | -1.53263 | -47.21848 | 2025-11-30 04:23:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e8acedf-2aa7-3527-ba4b-a91313461e1b | -0.95742 | -46.79819 | 2025-11-30 04:23:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 186029b6-b134-35cd-aeb0-2136186cd440 | -8.04529 | -43.12443 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9f313d09-9f54-3e33-b416-b19e5eda4364 | -6.49583 | -42.33492 | 2025-11-30 04:23:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e019efff-a09f-3a7e-abfd-a22eeca7fa15 | -3.42446 | -41.00661 | 2025-11-30 04:23:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 55ebc76e-2789-3153-bc8e-36c2029469da | -6.90867 | -42.8202 | 2025-11-30 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fd9eb2fc-2b32-355c-9ebc-e70560d0534e | -8.0344 | -43.12659 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 55c71ff6-41ab-3528-aab6-72fa470aee55 | -6.54783 | -41.70517 | 2025-11-30 04:23:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c8f07e04-0442-36f3-b6d6-321c8021be61 | 0.30195 | -50.87476 | 2025-11-30 04:23:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 241cb2dd-7cdf-3c3e-a039-c4ab5c272534 | -2.54103 | -47.79774 | 2025-11-30 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbb67902-c16a-3343-9856-2608ab21381b | -6.31992 | -43.8129 | 2025-11-30 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37d8e664-5000-37bf-8975-e7787c0024a8 | -2.63755 | -45.91974 | 2025-11-30 04:23:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 368f077e-5295-32d5-a445-80f3cafaa2c4 | -2.74123 | -45.21031 | 2025-11-30 04:23:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd1950aa-c6c1-31a0-87bc-44a95d710c1a | -6.31137 | -43.81187 | 2025-11-30 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32a6ca36-55a7-3595-b783-592ace233df6 | -6.68618 | -39.69479 | 2025-11-30 04:23:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fe3f6444-64d2-3aaa-be0a-01d776d534b7 | -6.71868 | -41.50699 | 2025-11-30 04:23:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d9aaff6c-d2ef-3798-b728-5b9f7f9d00b6 | -7.74684 | -44.19069 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ebed785-468d-3092-8fdd-147eda7fc6ac | -7.74405 | -44.18665 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0baa9ca-0777-3003-8c4c-a581dbffeedb | -7.75353 | -44.1917 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8127ad0e-1a53-3464-a7eb-4839417690e9 | -1.47282 | -47.748 | 2025-11-30 04:23:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d03357d6-2233-3853-8968-c77b747a230b | -8.16788 | -43.20771 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 31f33ac2-d6bb-3534-9196-0860b80fee2b | -1.47209 | -47.7527 | 2025-11-30 04:23:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c15921a0-99af-30ed-9fa3-806d115e3594 | -2.32176 | -45.84027 | 2025-11-30 04:23:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77dd3aa2-880e-3471-937a-881a90b350ce | -2.90344 | -45.26102 | 2025-11-30 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdc58427-0402-3eb0-a8a9-4189700d1456 | -8.17075 | -43.21198 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 5766699b-40f9-38fd-90dc-a6295c6697a5 | -8.16502 | -43.20343 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 29be7a9a-c9a3-3d49-9869-5e1b53314786 | -8.03784 | -43.12712 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3351e528-e1e3-32bf-93c4-ee9daf12d385 | -8.16388 | -43.21091 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 72a06cf0-2920-384e-98b3-5a4d0769956d | -1.15881 | -48.09362 | 2025-11-30 04:23:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce38cb63-5ade-3186-b799-436d28df4c72 | -2.32155 | -45.65047 | 2025-11-30 04:23:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5595b087-b07e-3ff4-b4be-f0e03f7cde72 | -2.57868 | -44.17023 | 2025-11-30 04:23:00 | NPP-375D | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ef758c03-4277-307d-942d-841b72b4eb1f | -6.11345 | -41.79384 | 2025-11-30 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b91f3e9a-23af-304c-901a-adec50707632 | -8.15007 | -42.94181 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5e728241-6a92-3335-a1e7-196636f38d8f | -7.74739 | -44.18716 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 966576fd-2625-3673-9e35-b27a4ab033b1 | -7.46046 | -44.74303 | 2025-11-30 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5df7fb51-c3b1-3d83-a69c-b16f25aa7050 | -2.17478 | -48.42082 | 2025-11-30 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f61340b1-d3ff-36e1-9d44-a4d8408577ca | -8.04351 | -43.13114 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| ad33471f-a525-3c4e-983c-3430283aaf17 | -2.80918 | -45.23935 | 2025-11-30 04:23:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4a479ce4-a654-36f2-9459-4d33935aba66 | -5.70697 | -45.63322 | 2025-11-30 04:23:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b0ce02b-363a-36f0-b564-e4e5772e6a1a | -3.43793 | -41.50316 | 2025-11-30 04:23:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 38a15ff2-64fc-36da-861b-45d4463a2c17 | -3.66462 | -40.96993 | 2025-11-30 04:23:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 857b4343-e7af-3dd6-a45a-b22f815af43c | 3.35288 | -51.32636 | 2025-11-30 04:23:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 513a244e-8c57-33c7-bc47-253afd78395c | -2.9023 | -45.26817 | 2025-11-30 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5458f1f-2529-31f3-ae36-d420ec843f7c | -2.35007 | -47.85728 | 2025-11-30 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0ea48ce-c502-34f8-b24b-36d78f7fd065 | -1.89966 | -46.44407 | 2025-11-30 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README12.md)
