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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bfc4e0c-1725-3c84-9d6c-3f58aa75f9ab | -3.21416 | -54.94555 | 2024-11-03 04:46:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea7a37a9-4f98-3b64-b4e9-a033416f760a | -3.21361 | -54.94838 | 2024-11-03 04:46:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b862a992-27ce-35f8-a070-3ac82dc6df99 | -3.21048 | -54.94275 | 2024-11-03 04:46:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb706ac8-b639-3e86-a6e6-2ec8f062b4bf | -3.21023 | -54.94495 | 2024-11-03 04:46:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c14c8ed1-26d3-3fae-89f7-f7f2f999fe3d | -3.20969 | -54.94779 | 2024-11-03 04:46:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3188799-4dc8-3784-b93d-a767f43620da | -3.20557 | -53.84856 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a66cf2a3-8738-390d-a5d4-2672556aa68c | -3.20488 | -53.85289 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2f71dcd-d93b-3b21-ba9a-a71cb0da76d2 | -3.20404 | -54.58324 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a30131b4-6e23-3a48-8dca-9277b306511b | -3.62931 | -53.96653 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad712b7c-6fa3-3973-94dd-d32deee758fe | -3.62634 | -53.96159 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2dce9ae3-b756-3139-93fb-635284dc8e35 | -3.58466 | -54.55985 | 2024-11-03 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d51563e1-9fa1-3ff3-9ef4-8c26cedf9bc7 | -3.58085 | -54.55927 | 2024-11-03 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb37c511-cb83-3daf-9cbe-5588e531259a | -3.56361 | -54.6434 | 2024-11-03 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6644cbb4-6948-35da-b23f-299bdf7616ff | -3.55979 | -54.64278 | 2024-11-03 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db5317cd-12ba-3672-8807-af17465bf567 | -3.55965 | -54.59434 | 2024-11-03 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1dc80458-c6c8-3c01-9ef1-536b22d30ac1 | -3.55903 | -54.64752 | 2024-11-03 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98396e12-6b3c-3c4d-a107-e018bf69b69e | -3.55582 | -54.59382 | 2024-11-03 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e22164e4-7f33-3eae-b461-d1f0cad35b53 | -3.55199 | -54.59328 | 2024-11-03 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 470e3fa1-9095-3a86-bf68-4566dfb14e94 | -3.51773 | -54.68451 | 2024-11-03 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 54329684-d4fd-359c-ba83-a4ffd6fddc08 | -3.41115 | -53.80685 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2d53616-e7d7-3d46-9d65-2951d2962785 | -3.40818 | -53.80204 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2aea933e-c28f-36f1-ae59-86a48ae751ee | -3.4075 | -53.80627 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ebe7ca1-d823-3eff-9a4c-26857b174297 | -3.40453 | -53.80146 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fea1e44-18a6-3a00-9c76-cc46e313bff0 | -3.40384 | -53.80571 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfcbb5c4-cde3-36aa-9dc7-4f47412089b1 | -2.36575 | -53.70617 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d43ac77-fb3e-3b2a-9bb4-8b0315a6904c | -2.31458 | -53.97927 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c09bfe55-9e49-38cd-91dc-a65db1abd60c | -2.29069 | -53.78108 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e95afe38-61a4-362b-8488-eb7549d0cc0f | -2.29 | -53.78548 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b82978e0-a9c8-345d-b0ad-f2500e6ba558 | -2.28699 | -53.7805 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1a1f495d-4713-3e63-a9a2-2d98e2caffb5 | -2.27262 | -53.7513 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ad55c31a-b8b3-3662-8be8-33e6815a427c | -2.271 | -53.73761 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6fcb82c-05c0-34d9-807a-4ab17074d905 | -2.27031 | -53.74198 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c18095eb-51ca-3a4d-958b-4ce320322ca0 | -2.2673 | -53.73703 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51348629-f162-3ff1-bbfd-90a3b13fd1be | -2.37634 | -54.27306 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b54e9ba1-ba20-3880-9ae6-90f67017d08d | -2.3756 | -54.27771 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a17e1d3-0f93-3b7d-8fd4-64cb7e4b3f13 | -2.26286 | -54.50069 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 400dd457-f20c-3738-9a2b-7f4c1a0c28c5 | -2.78688 | -54.00861 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e01f2dc9-4124-3842-9bc2-d2b5325ee9f7 | -2.77779 | -54.55464 | 2024-11-03 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96a40123-1c72-3702-94ca-9aff719193dd | -2.7562 | -54.42645 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 43c3c70d-abef-32ce-b321-1415b9823afa | -2.7555 | -54.4248 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| c3842e89-8fbc-3999-93fd-7b9952a703ce | -2.75546 | -54.43118 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 3293e48a-cee6-348b-9306-1b2387410f87 | -2.75473 | -54.42951 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| e2db543a-2970-377c-9847-0b551117604f | -2.7531 | -54.42118 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bb7c157a-fd9d-3314-9408-647aa1dac1fb | -2.75237 | -54.4259 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| cc23755f-2d11-3ded-b6b6-c3366b105676 | -2.75166 | -54.42427 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 31071060-21be-35e7-ab05-9a88b8f26f0d | -2.75163 | -54.43062 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 384e472b-3f3a-38ec-afea-16a131713c73 | -2.7509 | -54.42898 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| a2df504a-8ff0-3b79-85ac-7dc2f5943388 | -2.75013 | -54.43367 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 218a0cd8-5f24-3c8d-92c9-30a99afd193c | -2.74853 | -54.42538 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 7e01ddbe-534c-34ee-a950-d671250d0442 | -2.74783 | -54.42375 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 233cd9cb-021b-3acd-8757-9d64fab1ca15 | -2.7478 | -54.43009 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| e1e6f27e-a03f-347a-bcac-145ba18c9b34 | -2.74706 | -54.42847 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| a72cd7aa-c242-39ea-8a35-2ac46b5ce541 | -2.7463 | -54.43311 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f09536db-072a-3933-8500-1d8328440d00 | -2.7447 | -54.42484 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 7cdbfe5d-85b1-352b-b889-b243860e67cf | -2.74397 | -54.42954 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 15628d8e-9d80-309b-8bdf-c182fc0ab692 | -2.74323 | -54.4279 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 26539ace-f52d-32dc-bd30-afea91939a0b | -2.74218 | -54.12133 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d4697898-5563-30b5-b862-7cbde6b465c2 | -2.74014 | -54.42896 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f951873b-e1d0-3253-be02-138c38c75236 | -2.65634 | -54.34573 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a778f3a6-0b7c-3175-8fcc-fbd0216a24b1 | -2.65527 | -54.34816 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cfa95db-69ec-3f34-ba98-5f8c66d97d22 | -2.6414 | -54.26712 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d3b3bac-c767-3ce1-8223-53ab1698fc11 | -2.63834 | -54.26191 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 676a92b7-cd74-375b-b5a0-76fd1dddc832 | -2.6302 | -54.74763 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 47770d9b-3cd1-3980-b78d-d09f4241e374 | -2.59842 | -54.01959 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcb8159a-8684-3578-9045-3b3c59dd7fa0 | -2.59647 | -54.01739 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f18176d-ee68-32fb-8c4e-2f284cabf1be | -2.59575 | -54.02187 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 365ea4bf-4d65-35bf-b945-1e464b4bd57b | -2.59468 | -54.01901 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9020838d-0c90-3587-9bd0-d554fdadfbd7 | -2.57415 | -53.97911 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d515407c-48c1-3210-8fa2-2a30e6b1d31c | -2.55194 | -53.9986 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbb198cd-ade9-339f-b045-f9bc3d51c4fd | -2.55123 | -54.00306 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f65e382-e1ea-38ff-91c7-2460a9dedb75 | -2.54303 | -54.00649 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 830cdde7-bf0e-32dd-8107-e57fcc028b6f | -2.51368 | -54.11813 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e566d624-2fa5-371f-86b3-93ceb50ccad5 | -2.48395 | -54.01616 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ebd31ac-bce9-35fd-855a-93ad28c9679a | -2.48258 | -54.0169 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 92ed4842-7877-3273-97b5-d8d3bf91aea7 | -2.47884 | -54.01632 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 828197ac-1e32-39f0-b5c4-04b06ac535cb | -2.47699 | -53.97919 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 35482923-8b24-37fc-8adc-e3ee59634c19 | -2.4732 | -54.54431 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7312350f-a934-3992-9173-e4a7571d7aee | -2.468 | -54.06105 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c9b6bf1-f20a-36bf-b616-4b87538c16ed | -2.42993 | -54.51781 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 752df466-30dd-36d4-8eaf-5a047479baa9 | -3.11439 | -53.71581 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ea328de-4cbd-3c87-8159-049b319020e7 | -3.11371 | -53.72008 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63506bb1-46b3-313c-81ad-1eff52eee504 | -3.11005 | -53.71952 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 502d47be-c5d3-37b4-beb4-43740ac6c2d2 | -3.09978 | -53.71355 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e070b52f-faf8-3844-b08f-664a9c856994 | -3.0991 | -53.71782 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e061ef4-b5e7-3b99-8604-1d4b7e0b1058 | -3.09613 | -53.71298 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed7f7144-5c12-3534-b0b3-ebbdca46650e | -3.09544 | -53.71725 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f130617-737e-3202-a8ea-a4c12ac0a45c | -3.05808 | -53.90164 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f8421f65-f730-3e90-a665-9a27c59694df | -3.05499 | -53.90284 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91d047bd-f8d4-3715-84d6-42281a8fe944 | -3.01413 | -53.87414 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a1ea84d-f9a2-390d-b4a3-c49aed5bfe91 | -3.01045 | -53.87357 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ac7b7c1-1e4f-3a2c-9d7a-f95c9c6808bb | -3.00976 | -53.8779 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92767663-06b2-3809-9895-b7dda023f1ec | -2.98922 | -53.88808 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c9c2b42-a957-3dfd-8f1e-4d485229e8b8 | -2.97908 | -53.7402 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db67085b-61d9-34bf-9cc0-09006c259d59 | -2.96917 | -53.87161 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec7ab9cf-fb99-34ee-8e4e-e194e83d6534 | -2.96578 | -53.91618 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 008717ad-e131-3d33-b436-04d219ac762b | -2.96249 | -53.86613 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc3bac96-ae19-30dd-9c9a-953891e0b59a | -2.96178 | -53.87051 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0560a3b-10d6-3ada-a39c-e584fc48015b | -2.951 | -53.91377 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92fbb6ac-d823-3671-a80e-2536ce3b9238 | -2.94661 | -53.91747 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a406ba1d-7a1c-3e1d-a2c2-5ff8cdbdd9d6 | -3.08587 | -54.15611 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |


[Clique aqui para ver as próximas entradas](README59.md)
