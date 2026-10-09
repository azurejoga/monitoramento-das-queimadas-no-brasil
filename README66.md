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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6622ff3-535f-33d8-b662-609fe2229549 | -8.73794 | -45.14263 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| aed0a841-4b65-3ac5-aee2-1a4ec2208dc6 | -12.03611 | -43.44781 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 715d9e47-fc16-3fb4-8870-4a41f8688a14 | -11.6746 | -46.78017 | 2026-10-09 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ef5afcf-528d-3271-8bf5-42d1c5a79351 | -12.21541 | -44.61707 | 2026-10-09 03:45:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3296a15c-35e1-3baf-90bc-a8b5187408f8 | -12.00463 | -43.45026 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22cf0d25-f8c0-3b78-81c4-ba2d9def5fcb | -13.81892 | -39.90412 | 2026-10-09 03:45:00 | NOAA-20 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| dcc77c3f-464b-314f-81b3-57aaf86b519d | -11.1899 | -45.32327 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 81c83260-8fff-3000-8821-e10c7103d66e | -11.28036 | -45.20324 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64cab053-a602-37e6-a8dc-79d289bc9a89 | -11.27883 | -45.19918 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09218475-0a55-32ae-864b-d2b0615ff265 | -11.06118 | -44.06169 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a97d31a-8cbe-35c4-a63e-fdd3af398503 | -12.01172 | -43.46761 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddb4ede7-0eb9-30c7-97a6-69d9d34c298e | -12.01739 | -43.49268 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9573962-1420-3222-99bc-75fb8a0e11a9 | -11.01192 | -45.43547 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 506f878b-a289-3b0f-9444-3cf69de4f534 | -11.27808 | -45.20312 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ec6198d-5870-3323-b308-12bddf5ba751 | -11.75025 | -44.92941 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03e6464f-75ad-3ad1-973c-812990337bd6 | -11.00363 | -45.41621 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 08010ff1-a154-3792-890e-3d727be70b03 | -9.93762 | -43.56034 | 2026-10-09 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c55ba09-b509-3349-8897-fbe20bb0d838 | -11.09162 | -44.03956 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a92511e6-f08f-301e-bfcc-4d672001ff3a | -12.20937 | -44.61949 | 2026-10-09 03:45:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d95f69c5-c8d4-38d5-9522-59a247ab4672 | -9.34676 | -46.58526 | 2026-10-09 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f9b73fd-83c8-35d4-a9f9-da7ff4e2802a | -13.40629 | -39.79747 | 2026-10-09 03:45:00 | NOAA-20 | CRAVOLÂNDIA | BAHIA | Brasil | 2909505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f5c4b16f-3f82-3798-9039-07428923c758 | -11.00895 | -45.4212 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7d048b6e-3b0a-35ff-b302-4c5deb618287 | -11.57515 | -43.69548 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 586c66c4-9b0b-3961-853e-b09041e5154a | -11.83744 | -43.59609 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e51a66a-0db8-3076-9cda-15bd32420a7e | -7.25023 | -48.07341 | 2026-10-09 03:45:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 083f598d-afae-3384-a30e-f8c12aba9164 | -11.57623 | -43.68988 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30cee16a-68ed-33e2-b62d-ce84fad4656d | -8.98948 | -45.91156 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a09da618-a1af-35ca-8eed-957e92af750b | -12.02503 | -43.45177 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a073a492-2a23-37cf-8ed0-93db746037c2 | -11.25527 | -46.27586 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85fa7b43-6120-3a1e-8af4-b39ea3bbb69e | -11.76812 | -44.95494 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d1347f4-0c72-35c7-8fec-4401653a5417 | -11.65104 | -43.68611 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd38d42b-7d57-3cad-b1cc-22ee1b085d9e | -7.50919 | -47.33866 | 2026-10-09 03:45:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a4c25336-fad6-3b28-aed4-485c215c62cb | -8.95874 | -45.1786 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e51b3e6-4fbb-3406-85e1-4459b42dcbcb | -8.72708 | -45.16764 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b09cab4c-dda5-3d92-aee8-ef0633c72131 | -10.86957 | -44.80689 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f612ca1a-0326-3f06-9711-3e1cc4705606 | -7.47359 | -42.84601 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d5d6ca74-6eff-3a77-abbf-4edfe8cf9504 | -11.82677 | -43.59704 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4a6f897-b6a3-3e74-89c6-2296a0fe7cf9 | -13.4986 | -44.3734 | 2026-10-09 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 372e3697-c103-33af-a008-a21c8317166c | -11.19409 | -45.30185 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79310cb7-0935-3537-a59d-69bf7e9c12cf | -11.19324 | -45.30617 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55b20ef9-d4db-38ef-8e79-063f4abbd3f5 | -8.72959 | -45.15443 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e082b32f-c8fa-30f4-9017-ad4f8ceaa399 | -7.46953 | -42.83869 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| da5eafb2-01f0-34fd-89bb-c5cf3b759857 | -12.00062 | -43.47158 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 440de072-d6a4-3c14-bdbc-95afde8ea9cc | -8.90482 | -45.21714 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| a3175309-d66b-3a6d-b1b1-92992d42a676 | -11.9962 | -43.46756 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59f394f6-45a5-37c7-b65c-581228e689b4 | -9.93124 | -43.5657 | 2026-10-09 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b33b8415-aef8-3c6b-bd38-a6ff370f8294 | -6.96024 | -45.27753 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| db8ea71a-88c7-364b-8707-c7771bf9ab45 | -8.96633 | -45.17073 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 42152f3a-b761-3876-8968-8623a326c75a | -10.90347 | -45.52884 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d5ba9ed-4aed-3dc6-a6a7-f725bf4c4959 | -9.88758 | -44.79906 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d911291-eddd-3cec-9a61-21b071e2eeb1 | -8.9032 | -45.22592 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7a426525-8b05-3df4-b0b1-529095d3467c | -6.88346 | -45.89588 | 2026-10-09 03:45:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| cac16691-3233-3a7c-aee0-6f8fcc5a43a2 | -11.64242 | -43.70383 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d35397a3-dba4-3541-aef1-4dd906bc7230 | -10.32131 | -46.61361 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| deffd999-0709-3301-bc16-85953d884a9c | -11.99296 | -43.48469 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fd8eac55-9a71-33cc-96df-7657bbe9cc23 | -11.75801 | -44.95188 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3feab148-3a40-32ea-908b-1bebeea49e0b | -9.2755 | -45.64506 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8437043-dcae-3e96-97b0-5cec3edd8c63 | -11.2527 | -45.18233 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a8ba0d7-c87b-39c1-b42a-14f6f66d7d36 | -13.25553 | -42.25884 | 2026-10-09 03:45:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 41.6 |
| 3ba8fdc6-9638-36e0-9aea-f6146a2166bb | -7.39819 | -44.75861 | 2026-10-09 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0e13b317-6199-3e01-88f5-82242f7078f3 | -11.08547 | -45.15487 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7f453d4-7363-3f1e-83ea-2b04d2f1afc0 | -11.06478 | -44.06522 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc385ad0-1d79-3d92-b57c-c3a2cab6826c | -11.83573 | -43.60504 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 609c9b11-2edb-3b16-8ee0-ba6a5e459995 | -7.25163 | -48.0664 | 2026-10-09 03:45:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8887f74e-8b20-3fa7-a571-ac673f6e0837 | -10.59994 | -40.2852 | 2026-10-09 03:45:00 | NOAA-20 | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3e7211ae-2386-373b-a028-65f8cb8a3767 | -11.07611 | -44.09171 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c9d4a4b-b26a-3f6b-9abd-627f1dcf13f3 | -10.29814 | -46.59886 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1d66075-8b25-3683-93b1-f91fa74725ba | -9.83478 | -44.78616 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28866ea5-58ec-3b37-a177-adfb6856771a | -11.10973 | -44.00208 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4295e67-a909-377c-901b-2034b670f2b5 | -10.98872 | -45.40044 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27c55751-1f9f-3bfc-97fd-641ac1e41393 | -11.86406 | -43.56615 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a10a6c21-060c-3a82-98d2-94c0a17ff94e | -14.15736 | -46.34317 | 2026-10-09 03:45:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44998b4a-e5da-3525-972d-7bdef328ae88 | -7.48097 | -42.83458 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a00c22b7-b27c-3d67-ae18-f1fb7d6c1532 | -7.40327 | -44.76402 | 2026-10-09 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ab475b35-2dbe-3d8a-8362-40a7c8436c5a | -13.84935 | -42.64944 | 2026-10-09 03:45:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6cd8bf2b-957f-3e34-be66-fdee48778828 | -12.00117 | -43.46865 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3e524ca-0650-3e98-b33a-d8eeea4e0708 | -11.83354 | -43.58905 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 733994e2-8048-30ef-9d1d-c83e76cd4016 | -14.7856 | -42.89919 | 2026-10-09 03:45:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2d418c6b-8335-33ab-949f-844b6c55f2a5 | -6.87526 | -45.90451 | 2026-10-09 03:45:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 34c0815d-251a-3d1b-84b9-1d5a25dc71a5 | -8.73289 | -45.13707 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fe9f3ac0-d3de-3057-8f91-d9780e6c9bfe | -11.77249 | -43.53181 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cf9a1d9-d0a9-3456-8802-6da75b3117ca | -11.77329 | -45.56191 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79f7baa7-19c9-3a47-a6ce-5686314940cc | -11.76633 | -43.53677 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca9e3003-a950-3a4c-8639-5257ea88af1c | -7.47766 | -42.85329 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 89240ee2-6eef-3a00-ab04-2ae3ee4620bb | -11.86344 | -43.5694 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 92da8f57-7454-390e-acbd-087cd7aaf83c | -12.37389 | -39.47837 | 2026-10-09 03:45:00 | NOAA-20 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 801a3260-61e2-3723-a731-2ab35fc77b99 | -11.75092 | -44.92909 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17acae92-cc8f-3f26-bfe9-bd393bc64528 | -13.16112 | -43.28324 | 2026-10-09 03:45:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 8f3ef16f-50ed-3b97-b7b5-f082070194df | -13.62933 | -44.42452 | 2026-10-09 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5ac7ed2-7ad1-3a4c-96dd-80426587de0f | -11.05249 | -44.04958 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59952519-02ed-3984-93ee-92b3ecf33440 | -11.75925 | -45.48324 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3950e15b-42cc-35e5-b460-c6862d0f3b27 | -8.73874 | -45.13839 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1ed98744-f438-3eb8-8718-7e55aac4b2bc | -13.36205 | -43.89108 | 2026-10-09 03:45:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc160c16-ca10-3d8b-a217-0222f7e73f59 | -12.21473 | -44.62061 | 2026-10-09 03:45:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44dd43bf-8b5c-3a95-8622-8a2a0920f57d | -9.78977 | -37.32285 | 2026-10-09 03:45:00 | NOAA-20 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 641da6c7-b12a-3303-a1fd-8aea787a0c79 | -9.12529 | -45.83304 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35349bc5-12a9-3e8f-9100-9740565ee414 | -11.75735 | -44.95532 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba36ef14-926f-339a-9e2e-a3d64b1c6e2b | -14.03272 | -40.55691 | 2026-10-09 03:45:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2a8027cc-de1c-3cbb-b974-bc1ecc6b484f | -8.90442 | -45.23893 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb570545-234b-34c7-a485-b9633589da0a | -8.90233 | -44.93835 | 2026-10-09 03:45:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README67.md)
