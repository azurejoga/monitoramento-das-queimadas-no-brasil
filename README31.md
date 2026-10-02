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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01e5d337-3bfd-31ae-89c5-83515990b17d | -10.91664 | -43.84075 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9dd8766-58c6-323e-9248-056226ccc364 | -11.72686 | -43.42843 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6dc25349-1125-3db5-a272-310000de53ed | -7.86812 | -44.18152 | 2026-10-02 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 254e9720-b48e-3c9b-80b4-e0c1f7a45a3f | -11.26497 | -43.51367 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58a04ab1-8473-3c9b-9b9b-c896ad1d1414 | -11.1645 | -44.62124 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cfcdbc7-4390-3c93-a118-1fa7392a3702 | -11.25053 | -45.2272 | 2026-10-02 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2f62dd0-b5b3-3cac-8819-fdee608839c6 | -11.78513 | -43.57173 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9bf3d9d8-7cd4-3b9c-a55a-b9e10e17b4ff | -11.14133 | -44.60586 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7bedb2d1-cb25-3be2-b56d-8147cbc0bdf1 | -11.14744 | -44.60103 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2a685a0e-ea59-3f32-948e-34d7795c8b77 | -11.26325 | -44.25898 | 2026-10-02 03:55:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58cddff4-090e-3ba9-9a61-4a802ad07327 | -12.56561 | -43.0775 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| eddb670c-2910-32ab-8598-f113916220df | -9.21589 | -42.15821 | 2026-10-02 03:55:00 | NPP-375D | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3788082b-977e-307e-ac31-b85240fad4e5 | -13.85705 | -43.63769 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c255ec0-6b23-3dd8-9674-576933a0af1f | -9.80962 | -44.81073 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 578ffd3c-2cf2-3d7d-93ee-bb8dfb7aa749 | -9.07792 | -44.98843 | 2026-10-02 03:55:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71e48ef3-8f23-36d8-8242-02bb768cd559 | -13.33936 | -43.85985 | 2026-10-02 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f0626f74-c54f-3835-a412-865f54ba0f20 | -12.51937 | -43.10495 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3f93e2de-490d-35ed-b624-ab3e757a2aaf | -11.68503 | -43.60597 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 066c96aa-2e71-3232-99f9-932c1f8f6ef2 | -11.77959 | -43.57574 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 254f26fe-3532-32f8-968f-a64dae007b9e | -11.40785 | -43.40162 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fe48e52-e72a-38d4-b690-97a0beef45b2 | -11.71219 | -43.43057 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70b013b8-09a0-3038-83e9-4a80ffeea8ec | -12.57073 | -43.07449 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3b534ce3-bb96-36bb-98b0-05f08b7aa80d | -11.72512 | -43.43803 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5164c310-5f40-317d-9c0b-ef1296b6c38e | -11.78204 | -43.5624 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a2072b6f-4310-38f3-b627-9cb5d46d2a07 | -11.78889 | -43.57737 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 75f9a4b1-2d1b-3226-b051-8bc79fc332c0 | -11.46297 | -43.42891 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e3402a68-9b41-3976-9459-0f0a6cac3562 | -11.1405 | -44.61032 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6251745-9818-3c70-95e0-4f6526a6e495 | -13.3906 | -46.82159 | 2026-10-02 03:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e56ac35-df28-3146-bfec-ea722d719fc1 | -15.77457 | -40.77833 | 2026-10-02 03:55:00 | NPP-375D | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8af26f33-551d-310d-a7bd-6a88ac1d7224 | -13.49398 | -42.50622 | 2026-10-02 03:55:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b389b282-0ff4-3a92-809a-fc24bc915b07 | -12.66764 | -45.09395 | 2026-10-02 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc4c2ac9-0419-3637-8119-92ed664969ce | -11.1564 | -44.60883 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d79e3152-9672-303d-820e-6a64495aa9c4 | -11.78756 | -43.55846 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6732e5ef-a68f-314e-af02-657cb880cd3c | -11.70716 | -43.59018 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f42d11d8-2006-32ed-ae08-ce49073c40c2 | -11.26227 | -44.25796 | 2026-10-02 03:55:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2268bf31-a9f3-38e8-9b2c-9ab905ceb558 | -14.20758 | -43.62555 | 2026-10-02 03:55:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a8bf6f4-bd9c-3ce3-be89-c1d73fa844e0 | -11.77453 | -43.55113 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a6b193c-0b0d-3577-91b4-8a1caef692cd | -11.76384 | -43.58302 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ded6ad5d-41da-32eb-a9db-757c7e7aa84d | -13.01068 | -51.29344 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dc5032fe-b997-310d-8e50-3ae6f656dfdb | -7.88023 | -44.17365 | 2026-10-02 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0a66185-6c2f-3b4f-afbd-401be7e8fb80 | -9.52655 | -45.32492 | 2026-10-02 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0d1fa3a-9f9b-31ae-889c-fd8f08402c8a | -12.5299 | -43.09753 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e7fc6f20-53ba-34b4-9a67-27ea650dde2e | -11.66168 | -43.60189 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 9841654e-ca04-3e53-9508-68795d9af361 | -10.90613 | -43.844 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b79a33c8-89c1-3f4f-9429-77fd807da976 | -11.70097 | -43.51847 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7413c002-151d-309f-b22a-9605366e90b9 | -12.91151 | -44.81575 | 2026-10-02 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 083ce67d-b0f9-3c5b-a126-3d54be3f1aa9 | -7.75243 | -49.2064 | 2026-10-02 03:55:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 399d7f78-6d40-333d-ad05-d2ed1f641b69 | -12.32791 | -46.37703 | 2026-10-02 03:55:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fa72419-93e2-376c-9efc-010753c7bdc9 | -13.34852 | -44.43904 | 2026-10-02 03:55:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bca3f1c-8d4b-3230-9098-2908998e58fc | -14.69991 | -42.87861 | 2026-10-02 03:55:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 97dcf53d-2c04-367a-bc97-a5411abfc1a2 | -13.86139 | -43.63133 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6dbda777-8f93-3e16-b39c-f2356c4df092 | -9.84264 | -44.83669 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e157e60-dbf0-3916-836e-598cc6dd62d7 | -11.67568 | -43.60439 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 164428a0-51ac-3af5-9f73-6d8d1b532934 | -15.47996 | -40.76741 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ca349ba7-32c5-3baf-9e35-2b542a01cc43 | -12.91645 | -44.81671 | 2026-10-02 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79a19815-510b-3c75-b344-b9ad45e01341 | -14.20312 | -43.62468 | 2026-10-02 03:55:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a16dec3-8b31-36cf-98f0-913282667549 | -15.63515 | -43.23802 | 2026-10-02 03:55:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1976235e-fa77-347f-b307-15ae9243550f | -11.76014 | -43.44818 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0589e75-d327-3848-bd64-2856c9a4d52c | -12.53163 | -43.088 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fba9b0b5-0b15-352c-b201-48f8f3ea0f84 | -11.3088 | -43.5749 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5849d29-33f8-3743-975b-c3b40b59701d | -9.81992 | -44.84261 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99e1a565-b72e-302c-bf52-d55fbe5620e9 | -11.80359 | -43.57576 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 10bde4a0-0de6-3cdd-92a4-b1a4f83c3b36 | -9.52331 | -45.34239 | 2026-10-02 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 395466f5-c5d7-330c-876d-0b8be3b8558a | -11.74596 | -43.57578 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ffea89e7-c8b4-347d-9e11-63331c1dfec3 | -12.98035 | -51.29112 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 12be6b3d-5d2c-378c-b6c2-9cc8d81df34f | -11.77018 | -43.57469 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 35aa5b48-8428-380d-8b48-6bdd8d7dfccb | -9.8205 | -44.83944 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eaf181dd-fd1a-3e10-8fd6-8e987cdbef68 | -9.81425 | -44.81484 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8fd8fc3-3a63-37c4-b094-f760c7dcc00d | -13.86602 | -43.63948 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ad69ebaa-7fd0-34fc-8944-13adfec02671 | -9.82533 | -44.81335 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf3d1b99-13ee-357b-9c00-c655a2132d36 | -11.52599 | -43.51821 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d0e64f2f-be2d-3414-aa0f-74db5475acc4 | -11.12932 | -44.61432 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b24be3ee-2d3c-3c36-bbab-c89bab54185b | -11.68976 | -43.50117 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7017d84e-c1f3-331c-b064-3cc9ad055685 | -11.69142 | -43.59734 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5edf8821-070d-3c95-a541-5462289cdb86 | -11.74173 | -43.44473 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24b10d0a-d11f-31e0-a692-5bbe16a25a5a | -14.005 | -43.8229 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e3f80e7-9a7b-3812-b7e9-591f49ef7212 | -14.87177 | -40.69804 | 2026-10-02 03:55:00 | NPP-375D | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3857d389-1eea-3148-a5fe-9266354c2e7e | -14.04231 | -43.84986 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89f495b3-5a05-36a9-a3d1-70398632a154 | -11.25836 | -44.258 | 2026-10-02 03:55:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bb406e6-b480-3e7a-94b3-3c8afe86a60b | -11.77099 | -43.57032 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 350c4833-0d89-3859-a072-8ee222e85907 | -13.33384 | -43.86385 | 2026-10-02 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fc9431ac-1b92-3038-b704-945c98e534f6 | -11.13547 | -44.60932 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efe6c6de-ab50-3441-92af-5c381b1eccf8 | -11.42717 | -43.40039 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c30d9c1d-1325-34e4-a4c5-39cd6a3efcfa | -13.86154 | -43.63858 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2e39feb-e210-3740-b66b-f4958ca3f6ee | -13.3343 | -43.71025 | 2026-10-02 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c5e2c48-ca28-3a61-baec-f73c82edae34 | -11.69057 | -43.60202 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4bfa3830-f3a4-331c-9b71-f763314ffa5b | -11.74044 | -43.57961 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c735cf78-b3ab-3834-9bd4-f58444aae20e | -8.33022 | -44.1541 | 2026-10-02 03:55:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 956851cc-15c6-3b15-b861-a6a7e158eab4 | -11.72883 | -43.43731 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22014284-ea0c-374e-a6a1-bf1997bc02b0 | -11.73622 | -43.44867 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 304d5e6f-4b2a-3c56-835e-e119af9f9eb2 | -11.76989 | -43.55025 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4aaa9220-4f9e-33b6-8d04-0e9302ad33c4 | -11.76938 | -43.57901 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0edffa56-f0fc-3dbf-b2e8-fe15061e054b | -9.77306 | -44.80401 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea8c4326-9f59-355d-9d39-03cf52ac0117 | -13.00511 | -51.28415 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| fe666af2-8986-327c-9bc6-c94a618ec118 | -11.24934 | -45.20496 | 2026-10-02 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf6f0ac9-f85a-329e-a993-5e55ab9708d9 | -11.13847 | -44.59336 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 777afd24-c6a2-346e-9685-d4cfa0c45cb5 | -11.4722 | -43.43067 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 607e1153-a35a-3472-85b3-766ec99424cc | -11.23611 | -45.18921 | 2026-10-02 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea8df60b-5c83-303d-a2f2-475e77c7e747 | -11.79807 | -43.57972 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cc48b00d-9bb9-3c81-80e4-116692deabdd | -11.16505 | -44.6183 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README32.md)
