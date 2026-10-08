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

## Dados Diários - Página 196

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21781655-55f7-3138-8474-d0137f127a2f | -3.47992 | -50.08656 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 959de5af-4593-34eb-b272-8d54d0d551a0 | -2.99858 | -54.12099 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c180fc51-260c-3d4d-937e-5eeceaa6da87 | -3.5412 | -54.65866 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47f4e336-c2b9-36cf-9f4b-73a7cbaf844d | -2.99623 | -54.10046 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36b1534a-0771-3f70-a49f-6993fc176e9d | -3.51719 | -54.6632 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1c05371-c7ff-326c-844d-8ddd586e038a | -3.07006 | -54.25143 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b17ddc7e-e19b-383a-bc85-d2414c9ed93a | -3.09001 | -59.18677 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f71a8c80-1820-3059-860e-40e180e6b056 | -7.22203 | -55.10675 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 30082048-9d2c-3634-b5fb-8d3f8fac5dcf | -3.84904 | -51.9324 | 2026-10-08 05:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fec5dbf-3190-3888-ac4e-b461c9a73484 | -3.11114 | -53.7865 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2c461a1-c0cc-3bed-bb99-1586605c3644 | -3.83858 | -55.98433 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb1cc89f-1902-31bc-a9bd-292783a343cc | -3.12881 | -53.70357 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d696a97b-aaf6-3f3e-9dc5-7720b9191cb5 | -2.38542 | -56.13463 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e67bdbf-dc64-30e7-a836-a157a8263911 | -2.85023 | -59.26156 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2772491-5fd5-3650-8ea0-356294b0c470 | -2.82367 | -57.61179 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8666a453-e24e-36ff-9202-2a65c4790c1f | -3.6884 | -55.49028 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4631f72-a48a-3159-baff-40ff230895e7 | -3.54165 | -54.65555 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4927e07-dc6e-3e0b-b3ed-74d34aa49c55 | -3.09142 | -53.72325 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a5ebfb8-45db-3329-acd2-59fb074a831e | -7.38461 | -55.2105 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d13425ed-7574-3be1-a5b1-650e836bbe66 | -3.28999 | -54.02908 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00157699-d6d8-303c-8b94-7a6504318b7b | -3.10788 | -53.76137 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 007a2cd8-fd74-3707-baaa-a38ec3555505 | -4.09856 | -52.06965 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd3cf497-28bd-395d-8984-0dee8a63909c | -4.74887 | -55.65884 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e9879c29-dca9-338f-9e40-052695b1e365 | -7.20674 | -55.10574 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43e57ea3-3ae2-3e39-ac34-c3de6bf60561 | -3.08245 | -54.2404 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ad89700-7c45-39ab-96f5-9547be429f7c | -3.67136 | -54.50154 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c2dde35-cab9-3815-bfe6-305f70da40e6 | -3.28023 | -54.05861 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39879af3-d98f-3f52-b153-7165216c24d6 | -3.18135 | -58.64297 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de52d259-8517-3133-888e-75eeeba683c3 | -2.69768 | -56.53763 | 2026-10-08 05:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec2603db-40a5-3f91-a67f-9fb7d76b1356 | -3.03386 | -54.10276 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ebea689-73d4-3cc0-8bd8-9c877871b0e2 | -3.31326 | -53.86902 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2fcbc1aa-8ab6-3146-8890-7ba1a09eea93 | -3.57929 | -61.61116 | 2026-10-08 05:42:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4be6ed06-edb3-3b65-80ef-964d71ebafc2 | -3.55106 | -54.66316 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ab6204b-f740-374a-a117-f660340bd569 | -3.30656 | -54.028 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2847f8b-02bf-3d68-a7e5-622762bb697c | -3.58336 | -54.65837 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8fd55dc2-936b-3efb-b3b6-90125cc8d998 | -2.78472 | -57.64421 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f8b9a99-b4fb-302d-84ba-540715ebb838 | -2.84422 | -57.479 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e12fde22-e3b3-38ae-b322-2a0c94d357ef | -2.48844 | -56.10603 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 487f7208-05ce-36a6-aced-93d990e5e9d0 | -6.98976 | -59.10854 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d0db968-1403-3b00-a469-9c5740bce4af | -3.47574 | -59.5722 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9275eef2-63aa-363d-98c1-708f8109a180 | -3.85055 | -55.97782 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2e68052-c624-317d-871c-1beca682473c | -4.57054 | -54.95755 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30e481fa-af2b-3166-99a5-dfb7137fa2a4 | -2.92662 | -60.98805 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88e4603c-6ae8-3c6d-ae93-ad7e07db3df6 | -3.58724 | -54.30799 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d78d67c-0fff-31c6-82cb-d395d1fe25b9 | -4.91944 | -55.85797 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a8f892c-df35-36c3-b120-f94f499146bd | -3.53482 | -59.48605 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21145750-5791-3cfb-b1ca-abcafc698a67 | -2.98989 | -54.14296 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1e52e5bb-a850-3e12-ab07-9d0cd61a16dc | -3.30654 | -53.86463 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 371c6301-b676-3387-a783-e8d49ae9a2ca | -3.41812 | -59.5769 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bfaaf69-c312-3beb-a718-1009a65fb040 | -3.23227 | -57.87666 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7112aef-6d41-3210-81b0-72544e8c49b7 | -3.02122 | -53.89596 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4891c5e1-b270-3436-bb09-a4f297096176 | -2.05121 | -56.20358 | 2026-10-08 05:42:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1e170aa-8466-3e26-9a49-9f542a208461 | -3.54409 | -54.67476 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cc53921c-186a-30b1-a1c8-d2e2f17cc508 | -6.72882 | -63.0534 | 2026-10-08 05:42:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98fa34e9-c307-352b-b9b3-1aab2fcbaf3e | -2.99672 | -54.09716 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d41a1cf5-62ca-372a-aac2-afff7c1aa107 | -3.52139 | -54.67011 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95d87cdf-b725-3192-98a4-eda3a407e757 | -3.54545 | -54.66553 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a675fb06-826b-3933-adc9-b71a0b2cb8c9 | -3.70364 | -60.55341 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9d2e72d-eff1-3801-9633-72a501f1fe58 | -3.00104 | -54.10453 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1b47b46-de3a-33a7-8d9a-8658b6fae3cb | -3.28654 | -54.05275 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c25e878-2f42-3870-9d51-f0b84becabe2 | -3.03435 | -54.0995 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c4bd9be-f151-39e3-ad02-6109c9ca02fd | -3.07625 | -54.28198 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44deab51-f249-36ca-8068-ee6d905b4c5b | -3.16371 | -54.73037 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78b4266f-7585-375f-975c-b2bc08c42a58 | -2.98176 | -54.12484 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 11ebdae9-5dd1-3b5a-a2b8-aea5be136702 | -3.00868 | -54.1259 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc298da1-e50b-3f36-8ea6-cb6ce4d12d93 | -3.02855 | -54.10201 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e516415-a4ab-3953-818e-67f59c9e9228 | -3.08386 | -54.30282 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8af71703-aad7-3cc3-9213-e2fb6f990234 | -2.99386 | -54.07995 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 391fae0a-3847-33d2-aef9-05e4c0e114fe | -3.30956 | -54.70304 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05e8c59c-576e-3f58-9690-751f975fab16 | -3.27424 | -54.04045 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dda19bcf-037b-3c47-b27b-89bcc1280683 | -3.11064 | -53.7899 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 37973633-fb1c-3eff-a38b-6eb7c7f1904c | -4.073 | -59.84488 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 28cffea7-f99e-3a4b-b92f-e98bc0149ed4 | -2.84173 | -54.12631 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5b5f27f-d3ce-3b47-9971-86e4ba228ef4 | -5.68107 | -53.48969 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73899764-65b0-3f13-84fa-f9c5ea6fab4a | -3.2717 | -54.05714 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aef801cb-21b3-319e-9a88-fec19ca39d14 | -3.53692 | -59.47267 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41338be2-b719-3288-b3e7-b3b6d43bfcf5 | -5.29107 | -60.09542 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25632a65-0d03-3914-bd85-1203af9d54d2 | -7.00074 | -59.11732 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c0b624a-92f4-318c-8394-9b90ab607016 | -3.46462 | -59.5705 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56975352-39cb-3485-9ab1-7d62ca6bca03 | -3.1821 | -58.63805 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d24ed04c-940a-343e-af8e-3a6c2dc9cba4 | -3.5749 | -54.32116 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b14f78d0-3cbc-3f4a-b3f7-263f1b3a73b8 | -3.45267 | -58.06614 | 2026-10-08 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15d9180f-206b-3a3f-93d1-ed4af1781a76 | -2.77792 | -54.08966 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0a60d2d6-84fb-3cd1-8e58-fd555c0d354e | -2.82354 | -54.10989 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44dce057-2e79-3115-88fd-e3e95beaa4e7 | -4.15066 | -55.14071 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 28e40e0c-2ad7-3f0a-bd91-aea9ab13a4d3 | -2.87861 | -54.2047 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| db64064e-862f-30f8-93c0-e75787fa16f2 | -3.16785 | -54.73734 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 642798fb-f203-3721-bf58-da9ca9402ae6 | -7.18466 | -52.62392 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4633b14-205e-363e-82e1-f863b5f77e19 | -3.22816 | -57.87605 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3689e2d-66d0-38ea-8f79-c14adae85fc1 | -3.30843 | -54.05252 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60490328-2031-3746-a800-416036674481 | -3.27475 | -54.03711 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa45a6b9-7acc-36f2-8fe7-82c3c9f4064f | -3.96593 | -56.1231 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d92e3938-68bd-36fa-a67b-4df2d0a7518f | -3.28339 | -54.05212 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3369ea5-3a0e-3e53-bd25-17530da0685c | -3.28561 | -54.02155 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0327864-1c8e-32bd-828c-8b44a5aef52d | -3.70857 | -58.54901 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4295d542-d021-3b89-950d-14c5984f8394 | -3.11907 | -54.17601 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0f2a99d0-7286-3cd6-996f-37cc9c37bb3a | -3.01789 | -54.24324 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 105271ad-03a0-365b-8a5c-696d45b415af | -3.28804 | -54.00476 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc9f6f0e-e141-3953-9dfc-653a80ca99e6 | -3.26209 | -54.04842 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1124b1a-218d-38e9-83ff-abf6132fbe31 | -3.86651 | -56.0007 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README197.md)
