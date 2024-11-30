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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0acf443d-4d89-3453-b9ce-2956ac528f8a | -0.81751 | -51.59725 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcfcfd05-a5fa-3999-8018-960e4a1c36a5 | -3.65701 | -54.72124 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c3e1044-4462-33ec-b1e2-29e4eb1ad5b1 | -1.51149 | -52.56563 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4ef2053f-82c9-3502-802d-5b2282b6d3ab | -3.75356 | -51.13725 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c55bf96c-9a52-3afd-9223-790d81e38d2b | -1.51375 | -45.90054 | 2024-11-30 04:40:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a853b129-a548-399b-a70e-4e51a777679f | -2.46606 | -46.54181 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 334afc99-f2db-3add-9705-02ac23e4710a | -1.96925 | -48.43252 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 35761ddd-99ba-3337-9d17-dac4fffe0bb4 | -2.20332 | -48.34906 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a14e9c6-69a2-336a-82b5-7031e447d188 | -3.84425 | -46.53452 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 288ca9a6-3a64-3369-94d1-028f761520f8 | -2.58907 | -53.97329 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ade996af-6611-35a0-9e2f-57f205e86604 | -1.31775 | -51.73255 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 03aa17a4-532e-3289-9711-af4cc43de6e6 | -3.76861 | -50.17296 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 12904e86-0334-3aff-9952-9f57898857a7 | -2.23293 | -53.69277 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c70f62f4-82d9-31d7-bf67-a5f1a7f513ef | -1.40093 | -51.75338 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96bc5390-314a-3f76-a000-0dbe7e031335 | -3.98201 | -48.1959 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 676b92a0-2ee3-3098-abb0-6d244cbad392 | -2.29434 | -50.59466 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffb52a8e-77c1-347a-b5a4-f8d022bbc216 | -3.60676 | -54.21344 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93437f28-8e92-39ba-885b-26ddefd67ba4 | -3.44559 | -50.3692 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c64b17fe-2008-3544-bb51-01f7710baf7a | -1.2623 | -51.74667 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9277b74d-9d80-3909-9c75-e06bb3d1235d | -1.24169 | -53.35641 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99b2968e-de71-30bc-889e-81666c4ff15a | -4.87026 | -41.28951 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| eb4eee96-1c69-36a4-af0c-841cdc6b58d7 | -3.32405 | -54.17957 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b944d78e-6bc4-3054-b7e4-6ec3b28689f7 | -2.83874 | -46.85506 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9aec9641-efcd-3c2b-927a-91078039dacc | -1.72348 | -52.47905 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22efe40c-1001-331a-8462-948ec42f344e | -3.32598 | -50.21906 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d0a2905-7b23-3e68-9040-eaf8cf57dcd3 | -2.20269 | -48.33135 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4329b8c9-46d3-321d-85f7-d481a335fa25 | -3.64961 | -50.2154 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 427e9467-c223-3394-9745-fb14ed8a92be | -2.91955 | -48.33755 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a74612f-82e0-3093-a02e-90b65f627f63 | -3.77303 | -46.68753 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e2fd8f1-6d49-34f2-bb97-90704023268a | -1.26165 | -51.75085 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c66cf5a0-e032-31f0-8f25-09e2524f0711 | -1.24792 | -54.54721 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5ef15b68-7692-3588-b16b-6d3a23f4aed4 | -1.07451 | -53.62975 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 334f4ba0-0da0-30ff-ba20-3ea92c7fc215 | -2.73367 | -47.53856 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b70859e1-fc3f-3501-8ab3-2246235627d2 | -4.06773 | -46.68281 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b352b483-b08c-313e-a1f0-3fa837f473ae | -2.94142 | -47.99918 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe8f1f25-452f-331b-9fe8-b103a627bb51 | -2.69492 | -48.66542 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff945987-8707-3ef6-9bd8-2524ec3f26ec | -5.07659 | -44.99183 | 2024-11-30 04:40:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c0f1c716-f61f-3701-ba4e-3f8ef82281ef | -1.61724 | -52.28331 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0c2d12f-df68-32ab-919c-5a6476f2503a | -3.73695 | -49.94145 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3da97220-0bf6-327a-84b2-ba835bff3dcb | -2.02072 | -50.7724 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 41cc2910-02d8-35e7-b9ed-4ec1a7567a5e | -3.70066 | -50.23463 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c927d09b-23fe-385a-a6bf-8b944fb4aa4e | -3.31939 | -46.62468 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7366fe88-ef08-3739-8233-81ba69f8430f | -4.62033 | -48.02356 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a1a7e13-0c23-3f56-b9d0-30e8684bc10f | -3.596 | -50.35947 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 735f39d1-512e-3a83-b274-743ec3111abe | -1.34992 | -51.97866 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 39cea2d2-df8d-39e1-944a-292fa6d8b2f9 | -3.97745 | -46.72554 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e248f63f-14e9-3602-a475-3af51569069e | -2.34183 | -48.83515 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0faf82e-7890-3452-8c1e-9f3e285e5438 | -3.27654 | -50.53347 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7565808c-60aa-3dd9-b2a2-0a4379e1c898 | -2.1216 | -50.60149 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c96cfb1-6d59-3263-be2c-87c26f72e5fe | -2.84978 | -53.03204 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f864750e-3372-3fbc-ac9d-9a25e1acded3 | -3.76806 | -50.17649 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cd0fd8ad-b480-31f4-b957-7572ff5df792 | -3.43614 | -59.29097 | 2024-11-30 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8601ba9d-56d2-3e80-bb7e-564644faca24 | -2.19037 | -48.41047 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18d29a2c-6935-3e28-aa4c-d6c4f489361c | -3.0388 | -48.00745 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c9970bf-66b7-378e-8734-6de7ac5af03d | -2.67675 | -46.28139 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bb8be4a-496b-36c1-a4df-6fa393a20a6c | -3.37553 | -50.39855 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 296d8183-c586-35da-b841-892f7d6193b0 | -2.67794 | -46.27357 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af46ee35-68f4-3abd-ae4b-62fcb49f491a | -2.70339 | -48.58934 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b0695be-4a69-33b1-8cfb-19973b4956e2 | -1.18459 | -51.76895 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 29287c48-dec4-3660-bf5c-889c57018d8c | -1.39996 | -46.49506 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee562cfc-c3ba-391c-8e08-51607b7739b2 | -2.59831 | -46.57349 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d24b5c26-7cd1-3485-af9a-455f351ddb0d | -2.82916 | -54.03756 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70e9998d-68ac-351c-814a-5c3230d28aa3 | -3.07164 | -50.98643 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e836cd18-0867-3780-a1ed-61076b27e1b7 | -2.32453 | -44.8278 | 2024-11-30 04:40:00 | NOAA-21 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0fa45b70-296d-334e-a7de-014e649f3247 | -2.31475 | -49.07358 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51ae2efc-dce4-30ec-9295-f262432a7c0d | -3.98233 | -46.64698 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0680796-4f1c-35f3-bc1c-81fd8022b0b3 | -2.8416 | -46.85931 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2c8ec75-8588-366e-b1d7-a537a64c2452 | -1.22918 | -54.08392 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25064854-2f48-316e-90f1-467bca185439 | -3.76876 | -51.61915 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eded09f0-34be-3cd6-a73b-b71725446c1e | -3.70397 | -47.1361 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dea105d9-b6ef-3d15-b044-59a570425aa8 | -2.09942 | -46.57604 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73a15c2d-6595-3e46-bb7d-a1fae449e70b | -2.10545 | -50.34505 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0576fd9-d9c4-3227-8c82-0d2715e11608 | -5.74909 | -46.18271 | 2024-11-30 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cadc0f3d-0e58-3a4b-a4e0-4e30d8b08308 | -2.72447 | -48.62777 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a7b6590-dbdd-382c-9d4a-e5d83446f451 | -1.04622 | -52.41442 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f65d387e-cb8b-3de4-bb42-dd01e70311fa | -3.82768 | -46.90159 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 184dcfb1-200d-3113-ad43-0fc47860e01a | -3.41309 | -50.16076 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f415c6f8-5fb2-3088-8db2-91d9fd0ff511 | -2.70404 | -46.12458 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0597ef97-be30-335c-ad56-be569328ea71 | -3.98916 | -49.93839 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55fa1f46-c034-3151-91a9-7c26547838a7 | -2.93229 | -48.60419 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 282885a1-96a9-3973-a471-669ae1c5748c | -3.17409 | -53.63989 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6dc474f0-46e0-3708-9190-c2bf8250d6b0 | -3.07089 | -50.32539 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4d633f1-54d9-3a58-9b9b-0f703fb4d060 | -3.79739 | -46.69136 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54aee92d-3920-3e1d-aca6-dc6e92a6a728 | -3.34988 | -46.30656 | 2024-11-30 04:40:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef9ae8b8-e2fb-33df-b12c-2ce1bad76469 | -3.78925 | -46.69795 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 87c5c8f8-c023-322a-816f-a1331d7b93b4 | -2.35807 | -46.87796 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c77a42ee-b63a-3a0b-8ece-8ceefadcbd6b | -3.00479 | -53.23411 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efab1922-d42b-3eb6-b2fa-245536451680 | -1.28786 | -51.72501 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f3d1af76-1fc8-3faf-9d12-4f5ca435393f | -1.0697 | -51.76115 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a9ce23a4-52c7-3d64-ba47-1f0cc1d45655 | -3.76385 | -49.89975 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| edd7261c-d184-34af-9d0a-c2751b8c8231 | -3.38567 | -50.33438 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef0cd5a5-698a-3eab-9aaa-5abeb146a19d | -3.21654 | -49.83166 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38e9ca20-320d-37dd-9151-7d695bb592fa | -2.93792 | -48.63322 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9517eeb-4fc4-3ec5-99c1-57f98dc18616 | -1.6567 | -54.23829 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 268afb66-748b-3ecf-9d53-22d7a7568fdd | -3.37489 | -50.82118 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 06ee7281-3aa7-3a03-8808-e0cb65ddce27 | -3.89356 | -50.07019 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43c34d90-a874-30ce-a92f-02a8b4977058 | -3.18976 | -51.6124 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dd3baf4-8baf-31ce-a20b-5a9f3986e9a6 | -2.13561 | -49.50204 | 2024-11-30 04:40:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f24ae13d-41f4-3815-8ebc-2124256ed1e6 | -3.37888 | -50.421 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 852a0b97-6ded-38ee-906f-1f3b93a3e6f7 | -1.52899 | -47.06536 | 2024-11-30 04:40:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README70.md)
