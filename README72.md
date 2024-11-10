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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecadbea0-3405-30ca-baa9-de66d17a9b8f | -2.25781 | -48.7452 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 482148b8-c5ad-3673-bb3d-2792e42e894e | -2.322 | -46.4858 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3ede7ab-b1be-3eb9-ba5f-149f7ddafb7b | -2.67427 | -46.79864 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c17bac35-d485-3c38-84ce-ff19f15e1cc2 | -2.37281 | -46.74182 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd694da7-3c4f-310f-9d42-ef53d980c19e | -2.36922 | -47.92878 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f09928c-5e6d-3000-8e29-8c247cbb0608 | -2.50551 | -46.37919 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80d4698d-86d2-30bd-818e-a2d63707aa75 | -2.19795 | -48.13933 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2163ad2-951b-3f68-974f-c21b0c2a0cdf | -2.16043 | -46.67182 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 899e3b7f-55a3-38da-921d-e0c67c69de1f | -2.09738 | -46.53862 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75dcd883-3c36-3e4c-a3d3-38c93eb64e46 | -1.94598 | -51.09976 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5a582eca-8e1a-3d8b-b2e5-d5cbb6a2fadd | -2.22242 | -46.43237 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e23f8409-ce04-3f26-83e2-1547c4c536d1 | -1.2032 | -53.61951 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f5c9472-fc78-397d-af0c-af42a5e60eac | -2.42372 | -46.30193 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2e7e8f30-81ad-33f1-bf86-cfb6a8947ca7 | -1.13203 | -54.21404 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6393871-855a-347a-977d-141b7e6892ff | 0.69655 | -51.44228 | 2024-11-10 04:36:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 983af751-b288-31e8-a568-821e8b1ee2ab | -2.19136 | -48.37112 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12f947ab-f85e-3aba-937e-b6ef4c7c26ac | -2.03547 | -51.1707 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24a0b1c7-c4d0-3926-82d7-667cc1d4c2e3 | -2.08914 | -46.34369 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90eff8cc-7a0a-307d-bd76-12c500c45971 | -1.23503 | -54.15964 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b2e8493-797b-3a89-8dd4-a688d72d57a1 | -1.5934 | -47.57053 | 2024-11-10 04:36:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 389e5edb-e358-393d-b84c-d7f0ce0a85e0 | -1.99675 | -46.35683 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bdfae18-73f7-3114-97ba-ebbb0cd70081 | -1.46476 | -51.48171 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8f7e2ea-054c-3e1f-83f1-11c13356699f | -2.33818 | -48.94234 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9fb6036-719f-38c8-98e7-7a60b3aab27c | -2.5666 | -46.52996 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0016b766-6a61-3e74-9c95-f5cfa6ae7efc | -2.13745 | -50.14314 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e773fca2-2f8b-314f-be4d-7931f498364c | -2.09763 | -48.40956 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b92ad263-af81-36f2-aa7a-84062ab81e4e | -2.38611 | -46.47619 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b16812c4-c7c3-3485-bc0b-1a7cd656ac79 | -2.38144 | -47.93777 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b125f9ae-1f34-3bb0-b9d9-d622adf76fca | -2.18383 | -49.78628 | 2024-11-10 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e954d8fb-14b7-3fcf-92c3-94f1949b0d6d | -1.50672 | -52.15549 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d50e04cc-491b-3abb-8831-1d2c4dd70b18 | -2.15343 | -48.84924 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a927131c-0901-31a6-8bd3-80628db292f6 | -2.12185 | -48.55799 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16e62fe2-d31a-30b2-a577-ae3980f8ce93 | -1.13631 | -54.10134 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed5c1271-d051-35e3-936c-46fb6a936128 | -0.85593 | -47.63295 | 2024-11-10 04:36:00 | NPP-375D | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 685a92c6-82ae-342a-9ed1-2197e34a4c1c | -2.6845 | -46.80019 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7ec3c81-8ec6-3651-a305-ec1453f4b414 | -2.16201 | -48.5359 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfd46769-6de9-3ca0-96b4-aaf46b190e5b | -2.19816 | -49.12292 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c8b9d8a-1651-3b98-9db8-abb510cef087 | -1.55886 | -51.99712 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 503d3d72-7008-385a-919b-0453ea40ac62 | -2.37159 | -48.57963 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f09eef9d-596a-3c83-b027-ff9e23a4451a | -0.41168 | -51.48938 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83da7aec-a5ed-3d27-852d-58519951af7b | -2.10857 | -48.55593 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b96c206a-20ca-3a03-b933-5158f4be1208 | -2.04386 | -51.1638 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1863ddf-cdf8-3de9-b0fd-55a6b6764c87 | -2.39767 | -47.81247 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8888809f-f148-35d5-97f4-17fb67fcb319 | -1.49245 | -52.02789 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d727d414-db23-34fe-ad69-41372f1429ba | -2.38545 | -46.57097 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a169e84c-ec0a-32cf-bfc3-5e608c5864fa | -2.16724 | -46.69525 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec4b32d1-83ba-3e05-adc0-9ca5767f3eb8 | -1.6082 | -51.97975 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8818685b-ed13-3232-b3a0-d758b8a60ee8 | -1.99273 | -46.36003 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b7b42e8-8bc5-3599-b7c2-a9cd0abd8400 | -0.9479 | -52.44449 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d46c9e8-8ce6-362f-becd-fa270ff489f3 | -1.83926 | -52.15041 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86ca9bae-45ed-3f16-98f5-a813e08d7729 | -2.68734 | -46.80437 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f8d29f8-dc46-3d69-9bdb-4fc5a0847b55 | -2.61727 | -46.16364 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c057ec2-827e-3808-ba85-7fab6d4134cd | -1.87689 | -50.96263 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dce0bf34-c96f-3809-a012-396c5cf2cb61 | -2.41079 | -46.78867 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14c9cba9-4d41-3638-8532-649403c1aa28 | -1.16584 | -52.08879 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa5e5da8-2a12-3c77-94aa-d0dc13d54ba7 | -2.08381 | -50.34696 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3651195d-0af4-33c5-8142-ff60867c3e0e | -1.48246 | -51.74741 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b3ceeba-429d-3ff5-a2d9-e253cd49b09b | -2.20621 | -47.74027 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69c82814-241a-322a-b325-6e72ba00a751 | -2.15954 | -48.85373 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 419d57b2-16cd-3996-87cf-4ec7a3956d18 | -0.89611 | -47.69944 | 2024-11-10 04:36:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6eeb0c2b-ffaf-3661-a714-092a03a8952d | -2.68052 | -46.80333 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c67c371-b0b0-3836-a70b-2a62fa2fa06f | -1.6175 | -52.5342 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 547ef35b-58e5-30fb-92bd-b8e9b296957a | -2.51932 | -46.38131 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecc126a1-09b2-34c0-8a00-836f6792b772 | -1.71238 | -53.28298 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95624c11-c7ab-3b79-9aad-9a7b491cd3a7 | -1.27827 | -52.18424 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72d0f692-4c47-3046-922d-2371acadf536 | 0.05314 | -49.55317 | 2024-11-10 04:36:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5581668c-261b-3ddf-9134-d7914a2852fe | -2.28896 | -49.5364 | 2024-11-10 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 738133da-7cfc-3775-9c32-8f894055aa20 | -2.31087 | -48.53797 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88570d72-2c8f-3789-a4fe-74b4462ab910 | -2.20463 | -48.37318 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b9c12be9-28de-3d8b-82e6-a4b8ca49e8f8 | -2.14608 | -48.78787 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c139f4ec-187e-3481-aef2-b3218b09ea90 | -2.31345 | -47.42792 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ec7c650-85db-38ca-b712-44fa0dd0acb8 | -1.61573 | -48.67646 | 2024-11-10 04:36:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85dcdb4d-24d7-31f0-9d28-90c19ab857d2 | -2.29821 | -48.55365 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8afd3072-5bb5-3a4f-b727-075c06b3e5a3 | -0.14626 | -51.55901 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e0d0289-7b63-3968-a6d2-d0d1686a229b | -1.3975 | -52.3588 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4476e84-1610-3f8f-9a77-9eadbf87e332 | -1.48383 | -51.73874 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 639a07e9-de8f-3ea7-9f09-f919641d9788 | -2.31432 | -48.58086 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 333681d3-f7a3-3014-9770-e9bf7d78f128 | -2.36474 | -48.9252 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e3917e8-d778-317c-ba13-e15d3a0554a7 | -2.50617 | -46.30609 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42df4b57-4f8f-300a-8938-6dcd4525dabf | -2.633 | -46.79596 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49ac826c-4bb5-3446-893a-688886d084ec | -2.19905 | -46.6927 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b995e4b-7aa9-3edc-b6b0-168e10ac4c8a | -1.69661 | -48.16311 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6b46790-f173-3125-a1e1-47b6894e6b7a | -2.31001 | -46.47253 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bcaa350-64e6-316b-8877-21930d6343ab | -1.23895 | -51.75224 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01eddacd-c0b9-372c-8dda-f6db18967dd6 | -1.55074 | -52.27085 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87840186-d9a4-37d0-83ff-c653c7d347e5 | -2.17258 | -46.41323 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 851965f3-abd4-38ce-af6d-6c2213268f18 | -2.36484 | -46.7928 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 271e22cb-4633-3e9d-aa22-067f5f4200ee | -1.46408 | -51.48593 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d83a68b-89e7-3de9-8158-f13fd37b5d6e | -1.33809 | -47.68688 | 2024-11-10 04:36:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fb1376b4-4f65-3096-bd51-e46f8135cb9a | -2.08817 | -50.38589 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25b84b11-6f38-3c92-80eb-1ac7dbebccb1 | -2.18116 | -46.42602 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00713c6c-6b99-3c74-b11d-ec7158897be9 | -2.45345 | -47.1596 | 2024-11-10 04:36:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12f9113f-9e74-3f72-81ab-9dd458c27263 | -2.39889 | -46.77567 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96a9f566-3991-384f-ac1a-d8286a90ae43 | -2.16256 | -48.53245 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df874145-2bad-3f4d-9154-c6515f274dd8 | -2.49929 | -47.22844 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b5b1ad2-a3b2-3346-a6ba-fc917207a6c8 | 0.09466 | -49.85978 | 2024-11-10 04:36:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c4a396f-aac6-3913-87bf-f2ae46b60760 | -1.67243 | -52.0585 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 425c600d-1238-3050-bf4d-48446c674ff7 | -1.53354 | -52.20667 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9763cddb-e564-3d81-9574-5ade8a1c7765 | -1.47432 | -52.01769 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9525a580-a043-3a39-aa41-5122ea362d17 | -2.2181 | -49.87637 | 2024-11-10 04:36:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README73.md)
