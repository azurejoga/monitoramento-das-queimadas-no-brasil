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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09e9948c-592e-3cf6-b6ad-a6d7582b1773 | -22.80251 | -48.46476 | 2024-10-08 05:01:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3653a98d-0c1d-3faf-a3b6-65dcbe21a6a4 | -22.48325 | -48.37597 | 2024-10-08 05:01:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce67dfd2-4485-365e-930d-b3f778366bcb | -22.47795 | -48.37552 | 2024-10-08 05:01:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f82a392a-12b5-39b8-ac37-bfb1f3168e6b | -22.47399 | -48.36148 | 2024-10-08 05:01:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1ff2dc7-1b1a-300a-ae82-08d503f15e01 | -22.47366 | -48.36483 | 2024-10-08 05:01:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c53d9311-d324-3fdf-99fe-18c1dddcd0ba | -23.0773 | -47.30281 | 2024-10-08 05:01:00 | NPP-375D | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8c968696-ec75-32cf-80d1-e512f6606f37 | -22.65297 | -47.71289 | 2024-10-08 05:01:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9e256571-93ba-3266-9be5-02f671e7c049 | -22.64708 | -47.71627 | 2024-10-08 05:01:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 69a490d5-a8eb-3d89-9c02-8844795af272 | -22.18771 | -49.97143 | 2024-10-08 05:01:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| add20686-4194-3c1e-9de0-9db2b858a4c2 | -23.56688 | -51.42094 | 2024-10-08 05:01:00 | NPP-375D | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 650d68bf-d8bc-374c-895e-93e2336f234b | -23.31606 | -51.62815 | 2024-10-08 05:01:00 | NPP-375D | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a658ebbe-870a-3708-877a-2b0dc8ef5182 | -23.21015 | -50.89789 | 2024-10-08 05:01:00 | NPP-375D | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6c2061e2-a835-3e55-aff9-c8af83f95f36 | -22.81853 | -51.55768 | 2024-10-08 05:01:00 | NPP-375D | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a01279e9-c9a2-3242-ba88-f72b4b3f2035 | -26.60905 | -52.4832 | 2024-10-08 05:01:00 | NPP-375D | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cf7d2680-c8f8-345b-bf6d-deea011c8958 | -23.7046 | -53.21936 | 2024-10-08 05:01:00 | NPP-375D | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8c2ee5e9-3dd4-3dc3-b173-cdf2e222bbbd | -23.70276 | -53.21202 | 2024-10-08 05:01:00 | NPP-375D | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7f5d3646-639f-3c72-b4c6-1dc6807b260c | -23.70206 | -53.21749 | 2024-10-08 05:01:00 | NPP-375D | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 10ab9196-ec1e-33b0-b8ca-793975dd042e | -23.70132 | -53.2133 | 2024-10-08 05:01:00 | NPP-375D | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 87898c77-e594-3bcd-a13c-1b1c91cfcae8 | -23.11974 | -52.40867 | 2024-10-08 05:01:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9e40aad2-5347-3a6a-939a-9b46b7c2a131 | -23.11926 | -52.41254 | 2024-10-08 05:01:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d51ae461-c1ba-337e-80b3-34f3af9848bd | -23.11562 | -52.40816 | 2024-10-08 05:01:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a0787d75-6ec9-3833-8865-8429de6f4ce1 | -21.91125 | -54.60746 | 2024-10-08 05:01:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63c2cc61-7e9a-37ea-8666-dd072e3f493a | -21.90706 | -54.61126 | 2024-10-08 05:01:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d7029e4-a0ff-3cba-aef5-db109cd4be0e | -21.88567 | -54.6003 | 2024-10-08 05:01:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1dd168e-5be5-3560-afa3-9abd92a6132b | -23.35413 | -53.9082 | 2024-10-08 05:01:00 | NPP-375D | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d87fa9cd-c01d-3e3d-b543-0200288604db | -23.2541 | -54.93512 | 2024-10-08 05:01:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c9948e83-14e3-3c5c-8989-260079ba2ec3 | -23.25299 | -54.9325 | 2024-10-08 05:01:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6e46cffe-7377-398b-b660-003fb0cdfa88 | -22.90285 | -53.69031 | 2024-10-08 05:01:00 | NPP-375D | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cc2a4984-d7b8-3a5a-8b98-59fe7ad05ae9 | -22.89905 | -53.68973 | 2024-10-08 05:01:00 | NPP-375D | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c2e9861e-bd1d-3f78-ab14-f6c5000634ac | -24.25123 | -54.25996 | 2024-10-08 05:01:00 | NPP-375D | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| e2c2008d-87e4-3327-8494-6f6f01ce4bce | -24.24747 | -54.2594 | 2024-10-08 05:01:00 | NPP-375D | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 421641f8-8f97-352e-9f1d-1cdbd5ad7be5 | -23.90331 | -54.22439 | 2024-10-08 05:01:00 | NPP-375D | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| deb0886b-56ea-32de-a55e-75bdfc503a57 | -23.90269 | -54.22923 | 2024-10-08 05:01:00 | NPP-375D | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aa414313-2f12-3143-83f8-4c82ab3363b8 | -23.90206 | -54.23406 | 2024-10-08 05:01:00 | NPP-375D | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7266a622-6d0a-311d-9285-18eb271247f2 | -23.90144 | -54.23888 | 2024-10-08 05:01:00 | NPP-375D | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| fe40de6f-f098-3417-831e-3de7f7ed80ab | -23.89642 | -54.21859 | 2024-10-08 05:01:00 | NPP-375D | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7b8fe0a6-e151-3ad7-99fd-384ae99a68c3 | -23.88854 | -54.21971 | 2024-10-08 05:01:00 | NPP-375D | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cbdd963a-cfb2-3f05-9609-b78fcf900892 | -23.88831 | -54.22234 | 2024-10-08 05:01:00 | NPP-375D | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5a04e1ca-53c3-331b-8f4b-9b9b0f4e2614 | -23.8879 | -54.22452 | 2024-10-08 05:01:00 | NPP-375D | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e662c144-7978-3723-982b-e9846d05a581 | -23.88769 | -54.22713 | 2024-10-08 05:01:00 | NPP-375D | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 617a713a-098b-3da2-9e65-e04119ea9714 | -20.89567 | -54.972 | 2024-10-08 05:01:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffdce04b-590e-3470-b568-0271d2699b35 | -20.89217 | -54.97141 | 2024-10-08 05:01:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d691748-fc43-370d-a14e-a0b997f4d5d7 | -22.04031 | -55.94098 | 2024-10-08 05:01:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c76a5ac-d9c6-368d-9fe0-7ae9e2a452ff | -21.3493 | -54.60907 | 2024-10-08 05:01:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96db4f4d-c37e-300b-bd98-0d2134e8c073 | -21.34869 | -54.61341 | 2024-10-08 05:01:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e128adc1-6185-3a3b-ae3b-117c80939ab8 | -21.34512 | -54.61286 | 2024-10-08 05:01:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0470d222-1c53-3642-b3e1-ad456a9a31e7 | -21.3415 | -54.63853 | 2024-10-08 05:01:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d2c6842-5a54-3862-99fc-9b13e81d88e9 | -21.34089 | -54.64281 | 2024-10-08 05:01:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e133c06a-0e7c-3ad3-85b6-4eece9812438 | -21.34029 | -54.64707 | 2024-10-08 05:01:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 219c77ac-9efe-3ae9-b4e7-470b79e83e2e | -21.33792 | -54.63799 | 2024-10-08 05:01:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3dfe50d0-f514-335b-954e-203b02ba6850 | -21.33732 | -54.64227 | 2024-10-08 05:01:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b1b2f68-6a10-3ea5-80ed-8d38ed163aab | -21.33672 | -54.64653 | 2024-10-08 05:01:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c13104ed-679f-3463-8ddf-c0ed42d4909c | -21.33376 | -54.64169 | 2024-10-08 05:01:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8e717c1-3578-3eba-9764-d0e8c8f85df5 | -21.16837 | -54.63963 | 2024-10-08 05:01:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2249487-bc0b-33d5-b2ce-02e5b6eabef3 | -22.04088 | -55.93703 | 2024-10-08 05:01:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a916f9b-b00d-302a-a5d8-58e32f381987 | -21.39615 | -55.68266 | 2024-10-08 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c576c704-a0a6-3e44-ab12-83951318f959 | -21.39272 | -55.68207 | 2024-10-08 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 406fac6f-3cef-31b3-a551-54960aa48fe2 | -21.39214 | -55.68602 | 2024-10-08 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8bab2c4a-105b-3f00-9bf2-491817b39de7 | -21.38929 | -55.68149 | 2024-10-08 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b48b7f5d-fe6f-3e45-91e7-442a1412a8f7 | -21.38871 | -55.68546 | 2024-10-08 05:01:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7cf4090-114f-3f4e-8db5-9a3742cc7794 | -21.36297 | -55.69333 | 2024-10-08 05:01:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cb776c0-b2c6-3ac5-8112-b0c9c7460769 | -21.3624 | -55.69724 | 2024-10-08 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c73ba466-75e0-3b41-86e8-34120bf6808c | -21.36183 | -55.7011 | 2024-10-08 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 634f843b-ab25-31f0-b2bc-b7466dc5583a | -21.3584 | -55.70055 | 2024-10-08 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed5c03d5-abb3-30a2-abaa-bc8cf055f4e3 | -21.35553 | -55.69612 | 2024-10-08 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1774efb-9d30-31a1-98e5-e790f4554cd0 | -21.3521 | -55.69558 | 2024-10-08 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb61d5fa-8d14-3675-aa5c-f119d43df3ff | -21.32753 | -55.69557 | 2024-10-08 05:01:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c18c0aa-f605-3846-86ca-aa2eca0c3dfd | -21.3241 | -55.69498 | 2024-10-08 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cad30ce-b471-31a7-872b-0a40b6e841f1 | -22.7302 | -55.27794 | 2024-10-08 05:01:00 | NPP-375D | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 633af23d-dcc7-3426-9b71-2fae8260723b | -23.72131 | -55.2533 | 2024-10-08 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1c116ec4-ac99-30b8-8e9b-d2a3c037c62b | -23.24433 | -55.47915 | 2024-10-08 05:01:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c39e5216-de06-387a-bef5-d955690d82ea | -23.24082 | -55.47856 | 2024-10-08 05:01:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f8453f0c-d836-3c17-b7bf-d971b9e7115d | -21.43224 | -57.23023 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e4cbcca-325f-3a73-95a5-587e25a9f311 | -21.43051 | -57.24135 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be09e627-5d47-3274-b004-571d91732df5 | -21.43006 | -57.22219 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 594323e4-ff14-306f-a904-5b9c64afff15 | -21.42994 | -57.24506 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3c878b9f-4c9e-3700-813f-f988cfd93b04 | -21.42936 | -57.24878 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b8d8918e-9d88-33ce-b23a-36a6d9c7b141 | -21.42891 | -57.22966 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf9dbdff-e2a4-3615-b9d3-92d38e20bcef | -21.42833 | -57.23336 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c69cc01-bd35-3d70-8f71-f64b7fbf40d1 | -21.42731 | -57.21787 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb895e7f-0235-3cb0-88cb-4bf1b1ce0b55 | -21.425 | -57.23278 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ce7bd28-0e1c-332a-929f-ca3db2a50b03 | -21.41706 | -57.26186 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f8e089c-db8d-31c1-954a-f5f8dc8b178e | -21.41488 | -57.25386 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 625242d3-feb4-3749-bc31-739a0d278a86 | -21.4143 | -57.25757 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd8b6db1-6e3f-320b-8bef-d4a43b1e17e4 | -21.40649 | -57.26382 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd03f933-01bf-387d-b481-101163e6e179 | -21.40373 | -57.25954 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d88325d-0d57-36d4-832f-3368f961740f | -21.40316 | -57.26325 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c64d1da-62d1-3677-a69c-c3f2a0a6af0b | -21.4014 | -57.25981 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e321a4d-9c1d-32d9-8e49-193c51832677 | -21.39819 | -57.2364 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dffd656-724a-336a-b772-2792c5c79590 | -21.39645 | -57.24755 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96528eec-0546-381c-89ce-1022de5ff7f3 | -21.3953 | -57.25497 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60438a95-11d0-3b7a-a7df-07bad0f4cf14 | -21.39428 | -57.23952 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53ab3d22-d517-30fe-ba96-42424aa61f15 | -21.3937 | -57.24324 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2931d4da-5baf-367f-a4d8-055a5b04efdf | -21.39196 | -57.25439 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ffbc453e-bb6f-34ef-b3a6-f8350e2d7909 | -20.93782 | -57.83784 | 2024-10-08 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7914f85e-079c-3e1b-bf25-679492da9af5 | -20.87583 | -57.61003 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 04565db0-a695-3401-b47c-30dc18bb4590 | -20.87524 | -57.61374 | 2024-10-08 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| b68d7604-4029-32e4-9573-0d385142bf4e | -20.37 | -48.8 | 2024-10-08 05:03:29 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 326c88c2-3dae-3252-833b-4ae887365f4b | -20.37 | -48.86 | 2024-10-08 05:03:29 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c4a2670a-351e-3b58-af69-2d531d9cb020 | -2.43697 | -66.47655 | 2024-10-08 05:21:00 | NOAA-20 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README109.md)
