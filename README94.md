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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08629fe2-f5ad-325c-8b9b-a9c499559525 | -12.97104 | -62.79707 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8856427c-a00d-34b4-aa5f-bb1b1c3de8e1 | -12.97034 | -62.80095 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f65f12b-a92f-3b5d-82e2-93b421b54582 | -12.96966 | -62.68556 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f04b2fc4-0ad3-3a27-b18b-b806c603b89f | -12.96827 | -62.78853 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09dc886d-f987-3f89-9b75-96f3b9260f20 | -12.96757 | -62.7924 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 794c341e-a3b8-3645-a118-196650f81fdc | -12.96687 | -62.79628 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3a0fb9b-147f-33bf-8adc-ae253b2bf006 | -12.95794 | -62.65588 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c72216fc-a022-3000-9e18-67c8f4931f61 | -12.93953 | -62.53245 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd575416-1aca-3417-9456-2820ffecb774 | -12.93543 | -62.53168 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11981bde-630a-3485-8d89-159a6b10777d | -12.93199 | -62.52718 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c337047-c9a0-3f5a-bfeb-092082363a56 | -12.93133 | -62.53091 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76c93ac5-5c4e-33c8-9230-90f338d91de9 | -12.92723 | -62.53014 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d049e00-10a6-39c4-8e0a-fa765ae9c75b | -12.92304 | -62.50608 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f344c7fa-409e-3bef-8ce6-bfede159c39a | -12.91895 | -62.50529 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f4a2b9d-cb25-3440-aba9-b6ce54b56561 | -12.88814 | -62.79832 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b46f06f7-2714-339d-8bb9-40ada698c049 | -12.88327 | -62.80144 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28a25b06-8529-3752-8980-49f94cb69c0b | -12.76856 | -62.27365 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ac0ca3d-5d09-3ec4-8386-53cb1b32529c | -12.76793 | -62.27728 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0637bd0-8afc-36dc-a559-f90cec332a1d | -12.76729 | -62.28091 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c81d8ab8-8ac8-3423-90b6-02332b676923 | -12.76579 | -62.26565 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64673a21-4a5c-37e1-8d45-e2811b0e6883 | -12.76388 | -62.27653 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f7bbb3fb-49ce-33b6-84d0-939de5bd9529 | -12.76324 | -62.28015 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d7ef594-414a-35f5-a9ff-b4b9e7f45bd6 | -12.76261 | -62.28377 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7d22473c-4795-36e7-aafb-42e855dee562 | -12.7592 | -62.27938 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2626430-9512-353d-a7f0-1fb5d41fd1a1 | -12.75856 | -62.28299 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ac5c5be-8680-3779-83de-5baf0ebe4890 | -12.72116 | -62.23493 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2d26477-f51d-378c-8410-e87ae0e2e47a | -12.71921 | -62.24578 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8a4cf91-637e-3ddf-b0bf-734eace638f4 | -12.71582 | -62.24141 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e5f1bf6-f81d-30c8-81d4-99c238aac8b7 | -12.71517 | -62.24502 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28ce939d-43c5-332e-9e13-3142ac868198 | -12.82545 | -63.00278 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b70e0bb0-723e-3eef-a130-3edef0dd79f9 | -12.82194 | -62.99797 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2f58a1e-43f2-370a-957b-1a458730e627 | -12.8195 | -62.91504 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3d110e8-fb2b-3169-950c-ebdece86c884 | -12.81528 | -62.91429 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7325cbf3-a803-3c26-a5d8-caaa8a9f0e51 | -12.741 | -63.04247 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1f57982-9f44-3cff-9d13-2bb9d227db7f | -12.73747 | -63.03761 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8d36eae-5b58-3b36-8db6-458873100f78 | -12.73322 | -63.03681 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0d9d563-7478-3154-88fc-9d1fb7cfdfc4 | -12.71051 | -63.0409 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 228c1dcd-c2d1-3413-abfa-993b5f3145c8 | -12.70772 | -63.03198 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd69cae8-15ba-337c-8314-4ab8b0d8d2cd | -12.70699 | -63.03603 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7935c4dd-e025-3b17-8afc-95e7cc60a0c7 | -12.70347 | -63.03117 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59123a3f-eb4a-32d5-a8ea-b27f172ef81f | -12.70112 | -63.06848 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b90cc7b-d7f7-3aea-9d4f-fa05612ed2eb | -12.70095 | -62.97251 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee349174-49ac-3efc-b326-f8bfe0f9371c | -12.70022 | -62.9765 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c60cb963-9164-381c-bc08-156dd99c3de9 | -12.69922 | -63.03038 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d942888d-6a82-39ce-9e57-6d75f75f7dda | -12.69599 | -62.97572 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91fdd4c2-c81c-3261-9591-c984d1eac47a | -12.66406 | -63.07827 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f04f60d-de9d-3f6a-a739-6dbc03b6c1ff | -12.50792 | -63.26425 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b886237d-f426-3566-aa64-49bae52dee31 | -12.50714 | -63.26845 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee3f4ca1-cff3-3053-889a-0e2837433c18 | -12.50707 | -63.2661 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 310823ab-a8df-3184-b851-37031b666157 | -12.50632 | -63.27032 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47fd4078-e9a6-3027-8b55-150c848927c9 | -12.50199 | -63.26949 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c764677-20b3-33bf-9beb-6acf2fe9c2a1 | -12.48713 | -63.00571 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b62e25c-8950-3603-b798-164a6d33e89f | -12.48639 | -63.00981 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3c25eaa-fb42-334f-b976-e57f59cf7890 | -12.48435 | -62.99674 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 741fc28a-a413-3c3f-9436-bf6e7bcde0c5 | -12.48361 | -63.00082 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45e65de6-869e-3b61-92ba-76e9058d2e93 | -12.48287 | -63.00491 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b35910c7-99ea-3053-b6fc-184cd4366b2f | -12.48213 | -63.009 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20e3861f-85fe-3b93-9a47-04b869756c0b | -12.48139 | -63.01308 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b013888d-5e2b-3aca-b742-fa8da9f04a8a | -12.47935 | -63.00002 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c9c954d-1851-372c-b0f0-235453a3ecbf | -12.47787 | -63.00819 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72c0ddd9-8733-324a-bdba-05924603b459 | -12.47713 | -63.01227 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 756bfaa7-391e-3076-afcc-864316558f7d | -12.47639 | -63.01633 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c41fedd-ae46-3740-9828-bdd53a3220fa | -12.45881 | -62.99198 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93311643-411b-3761-ad14-e583b11e5a1c | -12.45806 | -62.99603 | 2024-10-13 05:06:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a168db97-54e3-3742-bbbd-b4c8e2c85a80 | -12.42458 | -63.98904 | 2024-10-13 05:06:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6549a860-abc4-3248-acf6-0f90cb56648b | -12.39525 | -63.73774 | 2024-10-13 05:06:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1bb6a197-9cb1-3f61-ac86-405e369d27fa | -12.39325 | -63.72323 | 2024-10-13 05:06:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c64c8e56-1b28-363a-bc7c-9c60ce70191e | -12.39242 | -63.72778 | 2024-10-13 05:06:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bbc4e212-3217-32e6-b617-552f939d1177 | -12.3916 | -63.73232 | 2024-10-13 05:06:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 014b6202-1f7d-3ea6-bcd4-cf7537f11489 | -12.39078 | -63.73684 | 2024-10-13 05:06:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f2ddeea-9170-3230-a15b-626d2e503c7e | -12.38996 | -63.74135 | 2024-10-13 05:06:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 280343d9-468e-3052-994f-1fa762fc0e70 | -12.38796 | -63.72688 | 2024-10-13 05:06:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf945c18-3b4f-3c31-b742-a59dab6dd38a | -12.38713 | -63.73141 | 2024-10-13 05:06:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 89de598b-1f76-3a53-8698-d1828a76d081 | -12.38631 | -63.73595 | 2024-10-13 05:06:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24fc4fec-e42e-38e4-afe0-d2970088b30d | -12.38549 | -63.74048 | 2024-10-13 05:06:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 288117e6-4339-3c72-8ed5-41269d7b6aed | -12.38266 | -63.73053 | 2024-10-13 05:06:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccfa64b8-508f-39b6-8261-719405017200 | -12.38183 | -63.73508 | 2024-10-13 05:06:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c865004a-a771-3338-9aae-b3b78b6022ef | -12.38101 | -63.73961 | 2024-10-13 05:06:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7396369d-aa1c-3ceb-b4eb-ec08f3baa02a | -12.35783 | -64.32379 | 2024-10-13 05:06:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1c41929-e513-307e-9620-7c408406119d | -20.47884 | -53.67421 | 2024-10-13 05:08:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59b21786-f675-3ddc-8d28-6222739bad62 | 3.52669 | -51.7681 | 2024-10-13 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6a1b54f5-c545-380e-a4ea-7babff8d6b9c | 3.52576 | -51.76875 | 2024-10-13 05:23:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| be51a717-234b-32cc-8669-432f7c80e5d4 | -1.05472 | -47.92976 | 2024-10-13 05:25:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4be29bc7-60e7-34b6-8be8-c072f71df98c | -1.05001 | -47.92289 | 2024-10-13 05:25:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7eab5221-10f5-3e47-8228-6e9f9aab10e4 | -1.04908 | -47.92908 | 2024-10-13 05:25:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 0f21e184-f567-3b12-b4f0-6e3cc8a01e4a | -1.04794 | -47.92849 | 2024-10-13 05:25:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 905d2ae4-aca5-3c37-8e4b-01ec547cdcfd | -3.22289 | -48.92583 | 2024-10-13 05:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 461313ef-dc57-3baf-98cd-752aed0f6aa1 | -3.22054 | -48.92655 | 2024-10-13 05:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 41881ffb-8904-37ae-a386-c207c34b1e89 | -3.21628 | -48.92484 | 2024-10-13 05:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 431f8814-e778-3cb8-aa5e-c4edfbc6eb08 | -3.15786 | -48.36699 | 2024-10-13 05:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1dcc73ce-708d-3db7-b6b0-473a96bb7f57 | -3.15691 | -48.3735 | 2024-10-13 05:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ac74904-3f95-3196-b5e0-dcc0deab9585 | -2.7495 | -48.40533 | 2024-10-13 05:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c0d62d9b-9fc7-31f0-8909-67b2ef487334 | -2.74859 | -48.41145 | 2024-10-13 05:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7da8ec6c-d0ec-3047-9e74-396c4414df05 | -2.17196 | -48.80946 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7892eb4-b75c-3aea-b4d9-d4c4901117a9 | -2.16453 | -48.81415 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d82b2a5e-9e0c-33eb-8cbb-bc044745e461 | -4.11367 | -48.24355 | 2024-10-13 05:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bb40314c-8bc5-3b4c-8b26-ad92ac854cae | -4.11362 | -48.23834 | 2024-10-13 05:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1c2ceb25-96e4-3780-96da-38f3690cbf0a | -4.11269 | -48.2502 | 2024-10-13 05:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a4419045-8c06-38ff-a247-1703d6b2cf69 | -4.11264 | -48.24529 | 2024-10-13 05:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f3ee5bfb-82e0-376a-9c86-8c184315c456 | -4.11175 | -48.2566 | 2024-10-13 05:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README95.md)
