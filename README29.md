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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a4efd6d-8780-3ce5-8c08-99ba05d8c59f | -13.76938 | -47.57031 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 553ccaea-e668-3b92-afd6-a93d68b190cc | -13.28862 | -46.9864 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70f49b9b-8db6-3d2b-adaf-0b2eb8e21ed3 | -8.45644 | -46.83617 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b4ad45e6-2165-388d-ad9f-ceae7ad5fd14 | -11.07974 | -48.36761 | 2025-10-03 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc3fa7a3-c5f0-3b92-8279-80e0ecad75a4 | -11.14406 | -43.39592 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f78ee6dc-1885-3016-88f5-9c24647802cb | -8.45553 | -46.84088 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4ae4b97e-243c-3645-b945-c0940b8e160a | -14.43974 | -46.37337 | 2025-10-03 03:45:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29d251e8-4b5c-3115-bc0e-99bcc2353fb2 | -13.98065 | -48.12513 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16732e49-9066-316e-9e70-58add20e9082 | -14.88278 | -46.84631 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a06db428-32c2-3a1d-9f5e-368e682763d5 | -14.56589 | -48.33204 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65b42c8d-bb56-35f1-af6f-c6da8e33ef18 | -9.91123 | -43.72067 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| df5c853e-c4ea-3d64-99a3-b10150e3e050 | -15.52208 | -46.81063 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6310d92-c835-37ce-a2fc-6d8627781c02 | -14.9149 | -48.29611 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8001ef84-f386-30fe-881d-08e5ebae18d8 | -15.28074 | -47.90753 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 16b2ec2a-d41e-33e8-8e43-4dad23db0f61 | -12.60535 | -46.97584 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 30becd08-d676-3113-9f6c-ed42e397704d | -12.80558 | -46.85537 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b91c2c92-802f-3388-874c-ad25e286b756 | -12.68018 | -46.8531 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7abec7b-3ba2-3f04-a24d-66f6e26256cc | -16.15831 | -45.11282 | 2025-10-03 03:45:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38d67466-d8b3-3c3b-ba27-ec23e910e8be | -13.79781 | -47.57701 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dede2301-8fa9-3001-9b66-56e18e6606c0 | -11.88183 | -45.02187 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 785e216c-afc1-3c20-8a83-79a5557262d2 | -14.86947 | -48.3083 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8883793f-2c75-3078-99b0-9071bcadce0a | -14.89423 | -46.84485 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 674cc424-10a7-3964-8567-390a3b7c98cf | -13.2659 | -47.2507 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7ec2ec7b-ace6-3523-8413-e1e433f9dc45 | -13.57602 | -47.28066 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3ca657d-0413-33aa-a9cb-77e4ea035a0f | -13.33864 | -47.79438 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5b34501-e3c4-3453-9cfa-d24803fd5893 | -13.79863 | -47.57297 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 47ca1a95-a4f4-37b2-97f5-06f1b921f1a4 | -15.94811 | -43.34527 | 2025-10-03 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ab5a91f-0b09-3c3a-bb32-93cb4b2a6b85 | -13.12891 | -47.87266 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0647c839-6c84-396e-9425-854cd83c5743 | -13.74232 | -47.99245 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a37631c-2fd6-3cc8-8920-666f8f739cec | -11.82497 | -44.91313 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84a2ca4b-87ad-3b00-aba4-52f15e12a3cd | -13.48508 | -47.25242 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b0e55d7-39ef-3bac-9e09-4e139c64dccd | -13.77214 | -47.55682 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f79216cd-1c4f-3eea-8e78-4691ca79c3c6 | -15.51113 | -45.91316 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fe0e5aa-8341-3e91-8e0b-c67102526362 | -11.47705 | -44.97546 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31e41411-503a-337f-be69-9f51ac8d9f7f | -14.23163 | -46.10431 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2e72920-c14c-3faf-ada3-b6045fc349f8 | -12.62568 | -46.96171 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1d3b143-6350-312e-b868-bd12d6a3540d | -12.61488 | -46.95718 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4254d7e0-644f-35ec-9f01-195c7f4d51a8 | -12.91838 | -46.37421 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65f27a5c-40fa-3fbb-8e03-32f6c426af56 | -14.97821 | -46.85681 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 306fb028-8aff-3ffa-9a0d-86b356d2d16a | -13.21122 | -47.82961 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 83c8f857-3c6c-381b-8fcf-5664a72e8731 | -9.3983 | -47.53971 | 2025-10-03 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 48200b2c-f372-307f-a060-a36aa0ea93b9 | -12.61926 | -46.9646 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 875872a1-09cd-3952-ac1d-fd85da31b621 | -14.44414 | -46.37864 | 2025-10-03 03:45:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b3fe6d4-8cd4-3e62-8510-757b7516d441 | -9.42468 | -40.72003 | 2025-10-03 03:45:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fd46d72f-b3de-3083-a495-b4af8e2842e4 | -13.31605 | -47.57718 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e75cb3a-deb4-3dff-a75b-bbf3783c7e40 | -13.56097 | -47.29669 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca2e2de0-0a5c-3d9a-8f0d-cd809f33f883 | -13.19882 | -47.8003 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 24e14fd5-d9b3-3ee1-a07d-0cd104170454 | -13.33662 | -47.23322 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d48b60dd-2d63-3656-be72-5d8fb31df64b | -14.85778 | -48.36312 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c02854e0-21a6-3da6-b8e9-e7ceb8d4b60d | -15.64561 | -46.25108 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0dc731c-d60e-3f83-9652-ee1355191e9d | -13.34669 | -48.10714 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b1ae113-c6c9-3dc8-9599-588df08fa610 | -14.87666 | -48.33217 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a71b67c-cb32-3e2b-aa6f-7e6527cdcd5b | -15.11773 | -46.6796 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4be7fe61-89e0-3986-a07b-a4c89d92ade3 | -13.5753 | -47.28416 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80690a31-014b-3374-81b8-5368626c10eb | -14.91684 | -48.34521 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0ef3744-3353-3f66-9085-69c68a0506d6 | -9.94936 | -43.72779 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 805eec85-0787-335e-bc9b-9f75830d371c | -14.91294 | -48.33458 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9231e6e2-6fe3-3e43-9b97-c6b40eeba3d3 | -12.79663 | -47.0164 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4418cac-ddc3-35df-bca4-8dfbc0666947 | -13.48209 | -47.25264 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e1b428bc-dcbb-32bd-ba54-168a6bc982d3 | -15.32728 | -45.05569 | 2025-10-03 03:45:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18ac09ec-f659-3f3b-b937-bc79e9448df1 | -11.4801 | -44.98711 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0a921dd-10b9-3e08-8683-cd883c168d56 | -11.91048 | -46.26834 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22780719-9e16-3c26-b973-0a16fd8d3402 | -12.92981 | -48.43355 | 2025-10-03 03:45:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 775b9974-38d7-3a4b-b08a-d0bce5138ac9 | -11.61679 | -45.06184 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04bf5743-784b-32e3-90d7-818f6a26b5b6 | -14.21872 | -46.08788 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d481a9c-16b2-39f9-9d2e-aef8db2d39d8 | -11.67514 | -43.2331 | 2025-10-03 03:45:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 650d938a-e5df-3b05-8c5b-345dffdeda5a | -13.19365 | -47.82579 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 699ddcc3-02ca-32aa-97b7-71b375ea5a96 | -12.4189 | -45.16479 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07f084bc-722f-3e40-ba1f-1cd743b39954 | -11.85073 | -44.96969 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7f400dd-6292-3323-8d29-27828ecd7262 | -12.9279 | -48.44109 | 2025-10-03 03:45:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7090734-9444-3bdb-87cc-e6329eb6aa7f | -13.33442 | -47.21479 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9d60e57e-c9fd-3ba6-94f1-917aa7f85faa | -13.12772 | -47.8784 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1135d65e-b92e-3c9d-bebc-fbebdb35c397 | -9.91247 | -43.74095 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| d47634e4-9fcd-3b39-9754-f1b5f5847c60 | -14.93675 | -46.88319 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ee7c0906-a61e-39da-8715-f6014205be48 | -12.83986 | -46.94552 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e91aa9e0-2593-3848-a887-95244b70adc8 | -13.48572 | -47.24926 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7616754c-298e-3466-8ff9-79e64cd403a4 | -13.24753 | -47.34441 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 200414c0-9bf4-371c-a1fa-b10226dabc12 | -11.67227 | -44.27293 | 2025-10-03 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50621d98-5470-3031-942b-838390b35846 | -13.96305 | -48.10141 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d1cd0e2d-7de4-3e42-82c1-b4051d4f2d3f | -13.33717 | -48.12326 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7aaddd57-e8f1-355c-81a2-e9648961c95a | -15.71585 | -46.27031 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 623b688d-23f9-3724-9426-7535cc5adced | -9.91306 | -43.7375 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 3db126a5-ff83-3d17-89c7-cb8e950382a4 | -15.80518 | -46.26163 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c40898d5-6c1d-303a-b130-472e8b77e94a | -14.44481 | -46.37527 | 2025-10-03 03:45:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 020c995f-07d2-322f-983b-b0aded5f03ac | -11.83459 | -45.02898 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 99dc37c3-e93a-3fdc-8f4e-c0bffa04ba9f | -13.77315 | -47.55187 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6c81f4c0-ec0b-3c3c-8aea-cf47c0f2af3d | -11.12608 | -43.39095 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7903f2bc-c58b-34f8-93e8-8c964bb98d5a | -11.17003 | -47.18017 | 2025-10-03 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4534c9bc-b739-39b8-a144-8f8741bf7f52 | -13.21701 | -47.83121 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7fa3f2eb-3534-3d71-a191-ba636b5b56fb | -11.80836 | -45.00196 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d31e9b8b-6af2-367b-9ef1-2acb0a0ef83d | -12.89964 | -46.89871 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5a3d178-8d88-34b0-9b9e-eb3bd65d37a1 | -11.45402 | -44.95901 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ae1367c2-0523-3b01-af81-219ac8d74ada | -11.72542 | -44.44176 | 2025-10-03 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ce6f730-6693-36f1-b609-f3934f419cc2 | -11.48516 | -44.98801 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d21b5b50-a73a-3440-a276-cf6e0ed13483 | -15.25166 | -47.92404 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 37881b52-5b51-3a8f-b0be-4e972524b9ee | -14.33275 | -45.86951 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 503b65fb-165a-32da-b56f-350955bf052d | -11.15759 | -47.1817 | 2025-10-03 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52cc1065-c3f9-3d13-88ea-60dda748a470 | -12.12077 | -43.4324 | 2025-10-03 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fecd294-0212-33fa-bdc3-25b9c2eb63e1 | -15.78863 | -43.72907 | 2025-10-03 03:45:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f28f91eb-76ad-3438-8127-f4b3024aeac1 | -13.02151 | -43.83838 | 2025-10-03 03:45:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README30.md)
