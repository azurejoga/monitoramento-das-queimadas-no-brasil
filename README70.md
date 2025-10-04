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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 206ab7f0-ddad-3446-8086-bff27b606417 | -11.68843 | -47.49748 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 17ecdbe4-46d5-3612-9a0e-cc47206cdcc9 | -13.32739 | -50.93883 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 508fab24-9deb-3954-ab59-ad2ef9b0d08b | -13.39035 | -47.55283 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3093e0c3-02dc-36f5-b3c4-65c1af703b58 | -14.8892 | -48.29197 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 87d30fc5-5993-3092-8f16-f4ac84ff1c93 | -12.37879 | -46.50998 | 2025-10-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7cf3c7e-264b-3390-8a4c-b965f7f0b40f | -13.97034 | -48.17836 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9abc72b9-52d3-3165-b481-7853c4d053c7 | -11.08383 | -47.88091 | 2025-10-04 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f9570c4-d08e-3944-9724-a8233ef3dd1d | -13.74125 | -48.09151 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3c0409ce-a0a7-3b8d-8954-5638bc781e43 | -11.91244 | -46.37737 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92bc4a03-cc0c-3173-9de3-6f1ddc4a307a | -11.0831 | -47.88524 | 2025-10-04 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12d8b4a2-d9b4-3a83-be06-f96ff58f1b65 | -13.33811 | -47.19603 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a5b2739-462e-3079-b980-1382d817dbed | -15.19246 | -46.39138 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3266131b-00ba-3ca1-b81e-19677ac207d4 | -11.804 | -45.02977 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06b7c4fc-1dba-31d9-bd21-992089bdf76d | -14.66317 | -48.31786 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| cea1d2fc-0b11-3ad1-9cd6-9036a1ccde66 | -13.66652 | -47.86977 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aeb415d3-3936-3cdf-9ede-9c0b9559c76f | -13.45224 | -48.54993 | 2025-10-04 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cd72c76-7f41-34d2-a948-9b241756b456 | -9.96033 | -43.69947 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2a5f870-5c6f-35ad-b4b3-666c3eb7517d | -11.11207 | -47.89571 | 2025-10-04 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 863a2a2c-c14c-3518-a602-d2771a1c987f | -14.74641 | -48.13731 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84aa6366-7ddc-32c5-8522-210fc2fd9751 | -9.10501 | -44.40096 | 2025-10-04 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 22373dff-4ac0-347e-93dc-168700349284 | -13.3296 | -47.62858 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 057c4852-17be-3c34-b150-8075206ecf0f | -13.34382 | -47.20501 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb906ef1-0b7d-3b98-a0f8-c079628d95be | -13.51979 | -47.30216 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b58dbfd-7247-34b8-b867-73d8392fdef5 | -10.35273 | -43.73077 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd016270-e6f6-373f-af36-f4cad5748b0d | -13.38905 | -47.28075 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ae9913e-c400-3b31-b14e-dfe5e4661192 | -9.31545 | -54.53644 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 00a3b230-7837-38dc-b2c5-2589ced12d6d | -12.08325 | -45.15576 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3bd5066-5f23-3de2-9f9e-c65754819843 | -8.64055 | -54.59176 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98eca51d-1d58-3b9e-a5ce-3e8d37924f26 | -9.6784 | -37.09194 | 2025-10-04 04:14:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d8468c07-280a-32f4-b7df-a4ed0191f53d | -8.90465 | -46.60366 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa918ae6-96cf-34e4-82e6-533ae6d44bc1 | -11.43284 | -43.48965 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d98b0708-800f-3987-bbcd-811d83847fa0 | -7.74409 | -46.30044 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3dda929b-f434-379b-abdc-5dfc45447986 | -13.29052 | -46.98128 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45b24e69-2d96-32c2-81a3-da38c6dfab7c | -13.74202 | -48.08699 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dae340c6-ad5e-3e4c-9456-7ef8870a18bc | -12.52725 | -45.97334 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f4a85cce-b85f-3736-80b1-d9a134d0edab | -13.6298 | -48.66961 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d327544-9107-3399-ad2a-f4adbbeb6887 | -11.2592 | -47.79163 | 2025-10-04 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37422e5c-0ba3-3fcb-830c-043d3f04592b | -14.91285 | -46.89165 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87d16d9d-7aff-3387-a949-2583ae9327f7 | -15.20711 | -47.1914 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86f5109d-224b-3da3-9aae-595e42e1bf6a | -11.54243 | -47.6735 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| acbc30a9-b0c6-31d7-8868-8ba608e22df0 | -13.73895 | -47.931 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 18c7f075-c6f2-3020-90d9-279a6a50dc4b | -14.86969 | -48.11815 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 851cfeec-bc35-3dd1-867f-0d658a4d2e1f | -7.73516 | -46.26537 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ea5d099-4f55-3c87-b3ab-6df990cf4fe6 | -9.44888 | -56.65759 | 2025-10-04 04:14:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cad2238-3a71-3796-a82e-544d0de319a6 | -11.10954 | -47.75087 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| b19c8d83-7685-3759-aa51-7243c7765e84 | -7.8649 | -48.21409 | 2025-10-04 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a11a717-25ab-3738-9903-7bc1559c2f21 | -12.84435 | -46.85373 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc13e9f9-e920-377a-b325-71edf1a4e44d | -11.5607 | -47.67698 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 230096d5-64d3-3dd8-a7a1-58ec48c1fb15 | -14.66926 | -48.26112 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7a3895c-e833-3832-882d-b467a163626c | -13.39573 | -47.28548 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f23ed4ad-f2a3-31c6-bf95-ee81e8da35da | -10.49184 | -51.51291 | 2025-10-04 04:14:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59a70410-f237-3de7-b78a-296558a535f2 | -14.96605 | -47.26725 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2834ce09-3fd1-3685-883a-710a6cdf4af9 | -11.92342 | -46.37522 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| c83ebf47-f673-3e46-b201-d674c16d0bf8 | -11.05829 | -47.78323 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31a67b21-8525-3a05-a8c9-8ef9bed5a384 | -9.33955 | -45.74454 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d89062df-adfd-3d93-b832-0937525d96eb | -9.42219 | -47.53258 | 2025-10-04 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2bef64b-c687-3390-bc68-83c3f3abe29f | -12.04249 | -45.19655 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a3d5a2fa-ea8a-3211-b6e0-dd21748cabd5 | -14.28056 | -45.8763 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 372f22ee-b355-3bb1-bc7e-6871edc2c8b5 | -13.10231 | -47.87798 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb481701-ae4e-3137-8b3d-876bf9112787 | -14.65373 | -48.3074 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8b5f9c56-8c1d-3a29-93ae-c75de430c344 | -13.60119 | -48.18478 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8c60b81-4a61-3463-a55a-539638ad55aa | -10.53058 | -44.5162 | 2025-10-04 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc0a5a25-928b-3ec3-a56a-31163c35813a | -13.17904 | -50.93077 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df0340eb-32ea-30e0-9fdb-96280400950a | -10.60892 | -49.14716 | 2025-10-04 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4851926-ada7-3300-a419-f01be59fc7db | -11.67707 | -44.27076 | 2025-10-04 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02a903ad-d75b-3f70-928e-a3afffbf1964 | -11.84391 | -45.03641 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7385ef23-c275-33d3-a82a-d50f8e869552 | -13.32679 | -48.12387 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46c8a702-2681-312d-9374-42de56d0e849 | -14.66061 | -48.28939 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68eaa75c-ca22-3018-a870-7efde69040d2 | -9.1178 | -44.38503 | 2025-10-04 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f97bb44-5040-33cb-b27e-78784555774e | -11.12525 | -47.84922 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c4ae680-283f-3543-b70c-ddb6025c7d80 | -9.12169 | -44.38207 | 2025-10-04 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac9dccff-5db3-3f40-909d-ca197b3eb372 | -13.30905 | -48.13925 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 035c7b9f-206b-3323-8675-5fa7884f41fc | -15.19522 | -46.39563 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06ff677a-3385-3ecb-b14e-8c7cf7c03fda | -13.934 | -48.14935 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb2147e2-1963-32a7-b853-479643a79bb9 | -9.94001 | -50.24675 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 142531b5-1a57-302b-95f8-ea301bf832d0 | -13.98856 | -48.18166 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cec24c10-8359-34e6-8855-e6aed020bb70 | -13.99564 | -48.20452 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 224f7af0-8222-34d8-9db7-136c52e126f3 | -11.91387 | -46.75416 | 2025-10-04 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e2d6b6b-df12-38a7-a532-18da56fb804a | -13.3447 | -47.24278 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56a53964-6aaa-3e29-a6fa-7328e0fb6a00 | -11.88298 | -44.98435 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 23984a26-b213-3680-8780-731f660b9133 | -9.3427 | -45.76846 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21f975ee-5c15-39e2-9325-44b72e3f3f82 | -8.1246 | -50.23307 | 2025-10-04 04:14:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b773fde0-41b9-3716-a1b5-ec16b5805df7 | -8.85169 | -46.74507 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e3a62b4-e3b9-3b3d-a87a-03ca2b6bcca1 | -9.34708 | -45.78493 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f0f0293-0995-302c-8f53-0dbe880b91c1 | -8.61643 | -54.98682 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59827599-5f0a-343a-ace1-2a409c083555 | -14.92653 | -46.894 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31c2ae2a-6e5a-3479-9dd3-f28c2a2e98b0 | -13.21336 | -47.82134 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 744eb0e7-66aa-329d-b014-b97a327c0c52 | -8.00728 | -48.53378 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3aa90f47-fc61-3bed-be6c-1f498d81132c | -11.54022 | -47.66425 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 33944d3b-39ed-31fe-91ed-9132bbba60dc | -13.81577 | -47.59 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 955d92dd-d954-3774-a1bd-4bfcc09fc954 | -7.74136 | -46.31705 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| a1c4e823-374f-315b-8cf8-b5c706202933 | -12.65471 | -46.96572 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 475b95e5-faf3-35ff-895f-26a553c554e5 | -11.9319 | -46.34557 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9305411a-fb2a-3c0d-89ba-3accfca6293f | -11.66338 | -43.27124 | 2025-10-04 04:14:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b8a12d97-4b53-3726-9d3b-129bd1baba9a | -11.33459 | -47.79637 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d2c304a-0ef1-31f5-9483-07069db571e4 | -12.84784 | -46.85425 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e1bae1d-bb63-3c15-bf06-b914d2033328 | -14.60558 | -46.73437 | 2025-10-04 04:14:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df7ddb68-3584-3f52-8edc-e5babcce2f41 | -12.64369 | -46.98875 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3a96a839-7f6c-32a1-befe-da50845ab0fb | -8.54071 | -50.16376 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a65842d9-890f-3ba3-be91-6126a83a86b7 | -15.25793 | -44.12178 | 2025-10-04 04:14:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README71.md)
