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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc181dd0-00b4-30bc-872c-2988f316f034 | -11.84222 | -51.29195 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 795f2ced-5664-3e4a-9cf6-af71c213302b | -11.84223 | -51.29567 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 86c951a9-e041-3616-a6f1-d8794e26d1b9 | -11.83255 | -51.28763 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aee53369-d323-3d15-b5a8-af79362884a8 | -11.38271 | -56.55125 | 2025-06-04 05:21:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e6667dd-30b0-3344-9898-66393e004223 | -12.51669 | -57.1864 | 2025-06-04 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7edc871c-409d-37d4-a72a-4fbedafb0568 | -11.9156 | -54.8114 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51cbe0c5-db89-3c2b-bf95-f8d407dce217 | -11.80077 | -57.35608 | 2025-06-04 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0824535f-6c36-3d8f-96d4-2561f391cd5c | -10.20902 | -54.29976 | 2025-06-04 05:21:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6d5fee7-18b6-33c0-85a8-fe8d67137812 | -14.03431 | -55.12671 | 2025-06-04 05:21:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f15e1ad-98b6-38ba-96d5-dc1ec4680db8 | -12.28848 | -50.10804 | 2025-06-04 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee3c0e98-79ca-39c4-bf4c-13f3f3b0b61a | -12.66598 | -58.21918 | 2025-06-04 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81b57169-8a69-3760-818d-49320a935829 | -11.80434 | -57.35663 | 2025-06-04 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b39799c-d799-3efd-8f24-cfe9aa5a74e2 | -11.9151 | -54.81519 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed3c5dc5-f4b2-30c0-bbd4-0328518aaafa | -11.91459 | -54.81898 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e902f7c-80ae-305b-ae76-a3c2b87c975c | -11.78641 | -54.7748 | 2025-06-04 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65199454-3f77-3821-83fd-3b30f0d74167 | -11.7008 | -54.55978 | 2025-06-04 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ee3525f-3fa9-3161-b091-048f8466f522 | -8.68733 | -54.87222 | 2025-06-04 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c195a22-2125-389b-bd9f-062ea009fed0 | -11.55821 | -56.42385 | 2025-06-04 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 758c97f2-7da5-3c16-9ceb-e23979da13a9 | -11.90683 | -58.679 | 2025-06-04 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6beacd0-be79-3c46-a53f-bd8515ec0d8d | -10.38566 | -53.514 | 2025-06-04 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f977a6f4-559d-310a-8e62-6fa43184befc | -14.02158 | -54.4725 | 2025-06-04 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 442ad211-a56e-31cf-800c-09bb28d6c996 | -14.01755 | -55.12425 | 2025-06-04 05:21:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4936da12-9123-3ebb-8658-4835dd748f28 | -11.91835 | -54.81326 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ed3b00e-9e81-317c-9c6c-81cf42951e55 | -14.01724 | -55.12558 | 2025-06-04 05:21:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4cf6cc9e-aeec-34ba-b7ca-ac000f197580 | -9.60132 | -63.25677 | 2025-06-04 05:21:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ddeeac0-a26f-346b-b687-3afc91027ec5 | -9.61904 | -62.81658 | 2025-06-04 05:21:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ad952f7-3941-33b1-bd80-d1ed2363acb3 | -9.62265 | -62.81717 | 2025-06-04 05:21:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbbb39d4-adc8-322d-8f0c-43018dbad0f0 | -14.01807 | -55.12028 | 2025-06-04 05:21:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f48f48b-b482-303e-851c-e6122acf7743 | -12.29421 | -50.10876 | 2025-06-04 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e774a99-c0ea-38f1-981e-ce3b8cda8f48 | -12.2775 | -50.10258 | 2025-06-04 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 184586ac-98cc-3855-bbbc-9f0b09e354b8 | -9.9621 | -64.93449 | 2025-06-04 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 700300a1-a100-3e02-b994-c56f45ee3f64 | -13.91174 | -54.66136 | 2025-06-04 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58fbea45-9450-32d0-b5ca-98f4347e1f67 | -11.83738 | -51.29169 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8a936e8a-62a1-3d6d-bb88-66b0a77f01f4 | -12.37665 | -54.16179 | 2025-06-04 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee2b7d87-b7fe-36b5-8afb-b82be768cb29 | -13.14521 | -56.80772 | 2025-06-04 05:21:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 380785ef-4968-345b-90c2-4ac31886c0c0 | -11.90077 | -54.78761 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3cf12337-7602-3fdc-bd95-06781f58cbdc | -11.89576 | -56.40684 | 2025-06-04 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 895914b9-87d9-3277-b62c-1f3201e3c5b9 | -12.31608 | -47.2624 | 2025-06-04 05:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a0019f8-27b1-3bd4-bbae-e4b7b7de9640 | -11.64578 | -55.36694 | 2025-06-04 05:21:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c68676f-f332-3ef9-8369-ff6f279cb726 | -11.38706 | -56.54739 | 2025-06-04 05:21:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f2b7615-b689-3435-b1e9-ea939a07e133 | -13.96459 | -56.77962 | 2025-06-04 05:21:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0438f12b-2ba1-3782-a82d-4dac7f609df4 | -11.83213 | -51.29086 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 877ea690-9338-3328-9ed2-e14738107349 | -13.09618 | -52.02173 | 2025-06-04 05:21:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60d80e6f-48a6-3274-9ef9-956f608d6188 | -14.01703 | -55.12822 | 2025-06-04 05:21:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47c76acb-f505-358b-9c89-927ec538323a | -11.83013 | -57.81733 | 2025-06-04 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8792f366-ee0a-3206-883e-e4ba676f310b | -10.7055 | -48.77804 | 2025-06-04 05:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bf00819-0ee6-3743-95ab-948d9f211ef6 | -11.8237 | -57.81229 | 2025-06-04 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0b0a98d4-70b5-35e5-b21e-e54f09e7e6dc | -11.90547 | -54.78439 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c16fedb0-803b-3451-bb56-cd2769a53902 | -15.27391 | -51.48051 | 2025-06-04 05:21:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94331c80-258e-393e-b5d0-23f66f3fae3c | -16.39745 | -58.17809 | 2025-06-04 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ca59c11e-0787-375c-911f-273c2ab80888 | -20.5437 | -54.11868 | 2025-06-04 05:23:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d4b3cb0-c974-3595-bbe8-f1f4882c0f8e | -18.71554 | -54.19231 | 2025-06-04 05:23:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2fdc5f27-54ae-361b-b749-2772b0f23d5f | -21.24227 | -56.15853 | 2025-06-04 05:23:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ba06bd9-f0f9-3c19-a091-222a90fef25f | -18.71645 | -54.18818 | 2025-06-04 05:23:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ab6d969-23c6-30fc-86f0-714184cdd975 | -16.39805 | -58.17378 | 2025-06-04 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 1cca217f-a6f9-3f82-92e8-274faaab89d4 | -21.24659 | -56.15918 | 2025-06-04 05:23:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4151feed-b354-3cdd-8d8f-5ede22dc2fe3 | -6.9791 | -42.9034 | 2025-06-04 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 8d38e1b1-64fb-3013-ba23-a06d8c65231b | -6.9602 | -42.9052 | 2025-06-04 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 107b2ce1-07f3-319e-980a-5b5457a584a7 | -6.9602 | -42.9052 | 2025-06-04 05:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 5ac9349e-4249-36e9-a9e2-6fcba9fdd6e2 | -11.69759 | -54.5612 | 2025-06-04 05:42:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a61942f-4bf9-3ddc-9eea-e64b643b5296 | -11.89763 | -54.79574 | 2025-06-04 05:42:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74266863-5903-3997-bcb7-58dc8820b789 | -11.55428 | -56.425 | 2025-06-04 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf411627-4f0b-33a8-9aeb-b405854fe3a9 | -14.56153 | -59.49655 | 2025-06-04 05:42:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b19d6b25-608a-311f-ad11-416f13ebf024 | -11.82778 | -57.81776 | 2025-06-04 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f2f9b7d-f0b6-337b-9567-01a7275d8f95 | -13.14703 | -56.80597 | 2025-06-04 05:42:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5abdf352-0bda-3a84-a40b-7073eb639db9 | -9.96133 | -64.96385 | 2025-06-04 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a25a24f2-cf4f-3b00-9d77-98acad7e0d6c | -10.49191 | -53.65627 | 2025-06-04 05:42:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e11e55f3-f824-3642-8f8a-4f682c7d045a | -11.89819 | -54.79078 | 2025-06-04 05:42:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3aae9b8c-2152-3d1c-8dc0-4abae8ad4b8b | -10.4992 | -53.65133 | 2025-06-04 05:42:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d87a4df4-43e5-3652-b2e5-ebc66b7e1c25 | -11.91477 | -54.81292 | 2025-06-04 05:42:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4d2ab22-8086-3b47-88cc-b9fb01d044ca | -11.82303 | -57.81389 | 2025-06-04 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac654bfe-c8ed-3359-97c1-119117e68aeb | -11.80128 | -57.35843 | 2025-06-04 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20c6133e-1219-36a4-9d01-7ef980061f50 | -12.64545 | -54.12456 | 2025-06-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8d50af5-7f66-3422-95eb-16225b2a64fa | -11.90106 | -54.78949 | 2025-06-04 05:42:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de04b3f9-b4b0-3892-af62-fc14b2baa388 | -11.90545 | -58.67988 | 2025-06-04 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a0f0fb9-10c2-37d8-8089-1385234a4f15 | -10.6899 | -57.64573 | 2025-06-04 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4fe04f3-806f-3267-88da-1a3ffce54304 | -9.41169 | -62.44516 | 2025-06-04 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 273a1d21-8d5d-3919-9f48-f3c576efa4a7 | -11.92103 | -54.81379 | 2025-06-04 05:42:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c374aad8-ea33-3ece-bdc4-4d750fa622a7 | -10.69465 | -57.64928 | 2025-06-04 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 606c896b-05b7-3a10-b457-4eb0919cc735 | -9.36762 | -64.45527 | 2025-06-04 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d6f8783-cf3d-312e-9286-be0520fe8716 | -9.96468 | -64.96438 | 2025-06-04 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42967abe-11fb-30a6-8673-0ab5b5f8f877 | -9.23994 | -63.29499 | 2025-06-04 05:42:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61dd0be0-c098-324a-8862-2568f07a26a2 | -12.66754 | -58.22058 | 2025-06-04 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b53f182-3e02-3529-98f2-ef46d1be7d96 | -9.96241 | -64.9347 | 2025-06-04 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5c8325b-062e-3671-96dd-22cce120c58b | -10.68437 | -57.64811 | 2025-06-04 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 735e180d-4fd1-3cb0-9625-8dcd179ce0a9 | -9.59989 | -63.25636 | 2025-06-04 05:42:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f28e3a3a-c05c-36f2-9ca3-ebbfdde9f120 | -10.69545 | -57.64326 | 2025-06-04 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc43ad07-38c7-3ad0-860e-e66fdef22f58 | -11.90058 | -58.67926 | 2025-06-04 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 554f6e02-31f7-36a1-99c3-2173424e389e | -12.6665 | -58.21884 | 2025-06-04 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9ff4568-2a7f-3c78-a90a-373913fb1f76 | -11.91064 | -54.81571 | 2025-06-04 05:42:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3445b3f-5916-3db9-aed9-ed953ec6a4ca | -9.62244 | -62.81441 | 2025-06-04 05:42:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd671224-5825-3d20-9e15-84edcf9e5442 | -11.56088 | -56.41787 | 2025-06-04 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ba98020-476e-3152-a0f5-b4eb3517cf77 | -12.27735 | -64.2748 | 2025-06-04 05:42:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53f86442-da11-323d-a304-a18a9ca442ad | -12.16939 | -64.19873 | 2025-06-04 05:42:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5394e472-5f28-3794-985c-a47108a9be0e | -9.62175 | -67.29144 | 2025-06-04 05:42:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1d7c66e9-5b91-3d34-98fb-5529599b4c05 | -11.70394 | -54.56197 | 2025-06-04 05:42:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf1ca469-932c-323f-a22e-5d3081f96648 | -9.33539 | -63.52157 | 2025-06-04 05:42:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 947308e2-62b3-3650-9027-397f53200f56 | -11.9142 | -54.81794 | 2025-06-04 05:42:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd37ff94-c211-361c-af49-81ffec7c92a1 | -10.38606 | -53.51088 | 2025-06-04 05:42:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 281a57ac-278a-3520-8f05-730c4f32934e | -11.63887 | -58.01517 | 2025-06-04 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README17.md)
