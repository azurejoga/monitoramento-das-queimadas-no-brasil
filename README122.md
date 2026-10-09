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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7620c581-024f-33c4-aef0-5ac07130af14 | -3.04937 | -51.22114 | 2026-10-09 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7eb94cef-3d64-35c7-ac15-38345b077e80 | -3.16713 | -50.44964 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e74808e2-fcd3-33a8-b79f-adccac25a399 | -3.19983 | -50.54993 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a297af2b-d976-36ad-ad75-38900aa12d27 | -2.82753 | -54.11538 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72de41d6-10a3-3000-ba19-62435f69d8a3 | -2.82729 | -54.13919 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4ca56aa-4992-344f-a1e1-223450ca42e1 | 2.42279 | -50.82441 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c71ff4c-a56b-3cad-b47f-24f24b764225 | -1.47406 | -54.54968 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 023a00d7-bec6-33e4-b0a6-c4c9f6f5564e | -1.50615 | -54.81434 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06048de7-17b1-30e4-ad32-5a092379383c | -2.9876 | -48.91288 | 2026-10-09 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36ee74a4-9ec6-3bb3-bc31-78eb3588057e | -1.52723 | -54.52338 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9269a45f-d21f-361e-8e34-4e9ec7bf83c3 | -3.1987 | -50.55706 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3db08c5-5d48-3c17-b7e4-27e59cb4bf4a | -2.48154 | -56.17548 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79ec7c2d-f91d-3add-96ec-d474d3721204 | -3.34126 | -50.40655 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51eabb53-1d55-39cb-b762-44ea8bf0b010 | -1.52346 | -54.56663 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34199c54-6b44-3de8-8f38-802dfdb59a15 | -4.09128 | -45.8993 | 2026-10-09 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3115f1bb-033e-3826-a96f-7fa2b9200deb | -1.46227 | -54.53045 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b5d4b77-d6d7-3423-9b91-16b920bc8686 | -3.36658 | -50.46897 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7284bc9a-8b27-3d15-b7ea-0b4f8a6edada | -2.4889 | -45.67437 | 2026-10-09 05:01:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f527d6a9-3ce4-3342-ac2b-35fa1c14e28b | 1.11757 | -52.49962 | 2026-10-09 05:01:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a49363d3-d1ab-327f-926b-fc8093e1c799 | 0.50298 | -50.77641 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3631a0de-0084-3c58-b675-ae3342954b9e | -2.7872 | -54.07428 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 546573be-b1b8-36d8-99f0-10ce148f9039 | -3.18017 | -50.587 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c9af93b-2854-3ed6-9767-ecf26e102d1c | -2.26357 | -48.05526 | 2026-10-09 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4861bc6-5c27-3b54-9d06-99eb1b93bd70 | 2.45114 | -50.81287 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23e4f8ee-9a39-3a35-a2ef-90c9bdc9bb55 | -2.73939 | -54.1262 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37884f2f-83e4-37b9-ac2f-b9d72a129dc9 | -3.18747 | -50.58449 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc4fc336-094d-337f-bd7c-8cbea179526c | -2.77731 | -54.06874 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee5e9412-a9af-3085-a437-a828bbfdc1f8 | -2.23789 | -51.92606 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8938f216-120d-352a-ac66-22ed9c2ac737 | -3.19083 | -50.54121 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2beae62-fab0-3642-af7a-773f3b2f18e7 | -3.17624 | -50.59003 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7579a277-630e-3c84-a15c-af5a2a7e92ad | 1.69383 | -55.61861 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3d7ea7d-b416-37be-b424-6129e353400e | -2.40144 | -51.29721 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 291efe8a-4ddf-3c22-89fe-ed867cf9c5d0 | -3.01532 | -51.01256 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| afdc08c3-78d0-3d4a-af45-02be930894c3 | -3.1897 | -50.54835 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8948502-782d-34ee-bb16-b0fe8fc6f108 | -3.19027 | -50.54478 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05c881dc-c75b-3c0e-be3f-9a7a7060030b | 0.98991 | -50.02508 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8a44353-e81e-32f3-a29b-82cc4c0affb7 | -1.36605 | -55.60521 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d6251b9b-4c8c-36a3-8374-927a9bd63bfe | -3.36378 | -50.48691 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 539d2f8d-dda9-39b7-abb6-25f21ec6ea75 | -3.18242 | -50.59464 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd8a5da7-4303-34a7-965d-3d495e1a1768 | 1.21946 | -59.97777 | 2026-10-09 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac73edc2-ce6c-3481-8eb7-1258b9b05cf1 | -3.17389 | -50.45069 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89b7f8c1-d8a4-3fbc-b113-3a4a2abe2bfb | 3.73951 | -51.61509 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfed2819-faa1-36f9-b895-07c2d5e6d025 | -3.17005 | -50.58542 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e40361e7-fcdf-31e3-abae-30d6033d6401 | -3.01197 | -51.01204 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a29970a5-eca8-3e86-b0cb-aec669d4a412 | -3.28786 | -49.50777 | 2026-10-09 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d303ada0-4185-3232-b122-11aa8e1f3bdc | -4.15725 | -43.18644 | 2026-10-09 05:01:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ab0ffcb-eab5-3ad5-b352-ae9d666f91b4 | -2.49533 | -56.06668 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 2d5735ad-8762-34b7-91aa-f7cb446702e8 | -0.87745 | -48.08364 | 2026-10-09 05:01:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6af312c5-b064-3fc1-99cf-cfe60bbea1c6 | 1.32242 | -60.71458 | 2026-10-09 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf42188c-c937-3671-bbb5-1db0861a5ad7 | -1.3273 | -56.40303 | 2026-10-09 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3d8992ec-fb09-335b-bcc2-2b52261f1874 | -1.21057 | -55.69797 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 246c718c-5b4c-3fc6-89ff-4d42728f7cc4 | -2.61364 | -51.21661 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcebfeb4-5d26-35c8-a6da-fa1028dd5ee2 | -2.74662 | -54.10349 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c9a49ed4-b268-34c7-bb6e-295eaa1a541b | -2.75301 | -54.04116 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 72f0113e-d7d8-3bc3-9d43-aba86896bc5b | -3.18298 | -50.59108 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1cf6495-fbbd-3914-a08d-3f1b52219a1e | -3.20938 | -50.55507 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e021faa-f990-3808-8788-de9d2039396a | -3.18691 | -50.58805 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0a4ee39-6b7d-3b9d-8867-0433402c7977 | -3.69685 | -47.67997 | 2026-10-09 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1bf70ded-398a-3549-a7e7-503938925ada | -3.21388 | -50.54847 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 369f1769-cc40-33c8-8a84-af7a3ce222a0 | -2.81952 | -54.09822 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a67d1b03-8543-38cf-8cb8-f41c497a65a1 | -3.20882 | -50.55864 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3029d438-6fcd-3af8-a7e7-7d742dc76afc | 2.42224 | -50.82095 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f191fb66-638b-3b84-bd4c-c7b75182b876 | -1.20899 | -54.22493 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92b740ea-5d0c-351d-a24d-b4e506fa40cd | -2.75199 | -54.09243 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a1ec5ce-d515-3eab-aba8-0ee27cc42629 | -2.48954 | -45.67031 | 2026-10-09 05:01:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2813c1e-5186-33dc-aae8-83383ce46165 | -2.7767 | -54.0726 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be5079a6-f797-32fe-8a2a-bd2567087744 | -3.18803 | -50.58092 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a9e308a-9578-38ac-b485-1ecc7763ac9f | -3.16375 | -50.44912 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 954761af-1c0c-3c26-8a3d-dc7011df13f3 | -2.74476 | -54.11512 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69f6c08c-a7ac-373a-b1ee-ae787a90de42 | -2.76003 | -54.10963 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2823225a-3f81-3e26-a83d-bbcb67c87ec2 | -1.33497 | -56.40366 | 2026-10-09 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4783cdb8-7305-3ca5-b2d1-4f35dbdff263 | -3.34741 | -50.47742 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4adfd768-22c0-329e-af33-3a7c786ae714 | -1.42338 | -55.71737 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d1677da-75ee-3008-b808-f7f9dcfe9e6a | -2.46867 | -56.08249 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1d56ca95-6f12-3044-9490-34ec663c6c67 | -0.39441 | -51.77138 | 2026-10-09 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 455bc6fb-6e08-37fd-8db0-8921e0003075 | -1.37914 | -55.45288 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f0d0822-fb9d-39bd-8c1a-a5570e3d59c6 | -3.25174 | -50.39666 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2991817f-20b6-388e-8aea-614281bd87e8 | -1.54064 | -54.55521 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c40d6974-b343-30f0-88e4-9f0bab75e436 | -2.475 | -56.06846 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 265d908c-1db3-34b7-a64a-bf9d666a2c51 | -2.08449 | -46.58065 | 2026-10-09 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9e7f69f-4ab1-38e5-9375-687719cbdc94 | -3.38912 | -50.21377 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fa89fac-c161-35a8-ba2f-83aaede13324 | -2.5068 | -56.14408 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de09d563-8e76-39b7-b911-f06861820eaa | -1.15106 | -54.21983 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 722819a7-7834-3c57-adac-ed6e3dcaba86 | 2.09214 | -50.89431 | 2026-10-09 05:01:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd893875-1270-3735-9bc1-5f5a0e612524 | 0.52292 | -50.77328 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 622ba773-924b-34af-9843-632fdbc390ba | -3.2185 | -42.96653 | 2026-10-09 05:01:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fecaf9c-b774-3c06-a48f-291a07065677 | -2.49494 | -56.16746 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e23125f7-7944-3f78-94eb-7172823816fe | 2.26268 | -55.98425 | 2026-10-09 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b3c32a4-0ed7-33c2-8281-36d3a9fe5c89 | -3.25342 | -50.40799 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b91274a-8393-3022-b7a7-283b77347d62 | -2.49333 | -56.17739 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 78e60628-e741-3fc2-ac89-c45f27648d4a | -3.2557 | -50.39359 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5864f440-7667-3443-9385-55d46cbee1d8 | 2.45169 | -50.81633 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ed2607c-8943-36cd-a524-eab2f290b8ca | -1.14972 | -54.21676 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bb908b6-c245-3e39-aa70-4adc1ca234a7 | -3.35706 | -50.41639 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81f27290-d532-3e49-ba7e-bd44df34bef8 | -2.7732 | -54.07204 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78f06d61-dccf-3b01-9d45-e3476e7465c6 | -2.83907 | -54.13309 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18c3df7b-364b-342f-a8bb-69ef9e62545a | -1.19724 | -54.20656 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 75add55c-5a78-3215-9f30-760c44c2ed6b | -2.73782 | -51.54813 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea75001c-d95a-3fd6-9ec5-9639b7eff18d | -3.69613 | -47.68472 | 2026-10-09 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ab3bd78-68e7-3793-8e71-f8511f6b04fc | -3.36037 | -50.4831 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README123.md)
