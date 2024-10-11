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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98473241-615c-37a6-994a-b1ff1f62434f | -8.14244 | -41.10384 | 2024-10-11 03:38:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7355b793-6c99-33f7-a052-c64bda392a8d | -8.00223 | -40.8487 | 2024-10-11 03:38:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ec301d28-3eaf-34ba-9c43-e23b15538e77 | -7.99873 | -40.84729 | 2024-10-11 03:38:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1970f7cf-564d-39d4-b2cf-325faec6c08f | -7.99531 | -40.97252 | 2024-10-11 03:38:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e923f2df-36d0-3f90-ba1f-7e647d43eb26 | -14.72733 | -42.29428 | 2024-10-11 03:38:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f5abee06-7122-3a37-97b7-37d473b86149 | -14.36548 | -44.66177 | 2024-10-11 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce6cb485-9ec4-3dab-97e2-983e0161b203 | -14.27418 | -43.7067 | 2024-10-11 03:38:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a48623c0-5953-386f-a5be-c699eab628c3 | -14.1901 | -44.37079 | 2024-10-11 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73f33d3d-4902-30a3-a663-e5df64268c6a | -11.68241 | -48.49015 | 2024-10-11 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e071dbfb-6279-3705-832c-80401d41101e | -14.18837 | -44.36976 | 2024-10-11 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7922f43f-c432-3144-b06b-4229e70a4093 | -14.13466 | -44.00148 | 2024-10-11 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 987ac203-0af9-3c50-aecb-53445c96487e | -14.04915 | -43.69239 | 2024-10-11 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| deba7073-fd3f-379a-98c8-82eb4073571b | -14.03966 | -44.16581 | 2024-10-11 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48859334-ad3d-3c25-87e5-98c14bc52590 | -14.00909 | -41.01458 | 2024-10-11 03:38:00 | NOAA-21 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 017966d8-c5e6-3a46-8788-12d99450f606 | -14.00841 | -41.01838 | 2024-10-11 03:38:00 | NOAA-21 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 96459add-0ee3-3a07-aaf7-b861f2cc2924 | -13.98811 | -45.79922 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e1583fba-8c52-3d05-845e-543bcd8efd08 | -13.98326 | -45.79409 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a4cba8e5-a4b8-3991-95fa-dd84bcb172ce | -13.98248 | -45.79798 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0a991809-453c-3af8-ab3e-54908c5cf09e | -13.98168 | -45.80194 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 830929c7-8b25-324c-ad32-3d36dedefb61 | -13.9784 | -45.78898 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 380df872-c385-35f9-a9d1-2a26665082db | -13.97762 | -45.79286 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bd5abbfa-4ca7-3338-ac0c-2bf71d1c884c | -13.97602 | -45.80078 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 63d79b5c-103a-3e16-87d3-403d76538286 | -13.97522 | -45.80478 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 670a9388-31d0-32a6-99d5-ef4d9b431738 | -13.97441 | -45.80877 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e6c3d2ef-5602-35a4-bd25-827b01630d1d | -13.97198 | -45.79165 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1d999746-c033-339e-b3c0-1691961a3c63 | -13.97117 | -45.79563 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5e2d0aec-1e82-3799-b089-2fe8ab9a24ca | -13.96956 | -45.80362 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b1ddc993-f2fe-3531-9e4b-dfe016766a16 | -13.96876 | -45.80759 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a1273154-f694-339d-9c3f-fae2c54b6019 | -13.96796 | -45.81154 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 89665dc1-921a-3771-b9d5-8d77b93a3863 | -13.96472 | -45.79843 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ebfcc0d-c70c-38a1-9ac2-0651e3f8c67e | -13.96392 | -45.80238 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8046588a-f8e8-310a-9777-d08b98ffa4c6 | -13.96312 | -45.80634 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5099e71b-c35d-3b29-8571-8a96cf151b17 | -13.96232 | -45.81031 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50cd4e2a-d4b0-3e76-922c-d26a504187d7 | -13.95828 | -45.80117 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d918701d-c5c2-3c80-a8b9-25bfa27cd001 | -13.95747 | -45.80513 | 2024-10-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b7ed6b17-0192-30a5-8bff-292289e825d7 | -13.92189 | -43.81522 | 2024-10-11 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d506744c-b5f6-33ad-a45c-8308755b5d7f | -13.92132 | -43.81816 | 2024-10-11 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b13bbed-a4bf-3599-8cd9-72d1a8629241 | -13.91691 | -43.81423 | 2024-10-11 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a5cd1d5-f36c-3b1a-ab2b-5b3c09a5b3ad | -13.89749 | -41.29434 | 2024-10-11 03:38:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 566c0bcb-bd82-3ce7-b1f5-873bf6020129 | -13.89725 | -41.29433 | 2024-10-11 03:38:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 12320d1d-9355-39d5-a0a3-aa9f78f7af6a | -13.81055 | -44.64053 | 2024-10-11 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 904d25cd-a2fd-3b77-a24f-b6d512c07acf | -13.81012 | -44.6377 | 2024-10-11 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 846928c4-de64-3961-9000-573b68a7bbb3 | -13.80946 | -44.64096 | 2024-10-11 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 997490cd-a841-31cb-8a39-1c868cf7951e | -13.74745 | -44.46205 | 2024-10-11 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6150224f-f96c-3441-b8bf-c3111c860aa1 | -13.74682 | -44.46522 | 2024-10-11 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 232cfedc-ea03-31d5-a5de-b1142498cdbf | -13.74158 | -44.46428 | 2024-10-11 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0f52591-9304-3648-935b-b07968e5e44c | -13.7414 | -44.46383 | 2024-10-11 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2b3a15d-3540-3bcb-b4ce-8159a8caf623 | -13.74094 | -44.46747 | 2024-10-11 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c3b5121-cd95-385b-8e98-7c441caa9557 | -13.74079 | -44.46703 | 2024-10-11 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 318d29e4-0a4e-3405-8d0f-4cdcd2a9c53b | -13.70672 | -44.44698 | 2024-10-11 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 459a4ee9-dd11-33a3-87c5-13764bdf634a | -13.70606 | -44.45038 | 2024-10-11 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 001f835f-5a41-3fb6-9d1f-78b1df49c785 | -13.53165 | -42.55823 | 2024-10-11 03:38:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 458d040d-db35-3cba-85d8-2305914eb651 | -13.46975 | -42.58162 | 2024-10-11 03:38:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b2385e78-1259-3b5f-9294-1c089270dbf4 | -13.36962 | -44.7767 | 2024-10-11 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 35214464-f99e-3bb8-a74f-a77f9c20ccbb | -13.36894 | -44.78013 | 2024-10-11 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 891e932b-0ac7-39a9-b854-8b0d63edab05 | -13.11588 | -44.07678 | 2024-10-11 03:38:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2dab86cb-4fd6-302c-a3ee-0e83af0e4507 | -13.07512 | -43.37461 | 2024-10-11 03:38:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52240d85-fed5-34c7-aa60-5aa1720d98c4 | -13.07385 | -43.37283 | 2024-10-11 03:38:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0294d170-0655-3455-9e51-268d19037dac | -13.05212 | -39.97163 | 2024-10-11 03:38:00 | NOAA-21 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4cd59467-5d62-3f0f-8f38-b890c983c66e | -13.02335 | -42.66516 | 2024-10-11 03:38:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9c52d892-8c05-3f12-9372-dcab6272539a | -12.96003 | -46.18658 | 2024-10-11 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6e7f80b2-496a-3731-b76e-ca0d76403f92 | -12.95907 | -46.19141 | 2024-10-11 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b6f2da34-05c7-3ef9-a28f-193b2dfbb304 | -12.95777 | -46.18661 | 2024-10-11 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3f3a75bc-c24f-3ff1-aa54-9950397ef689 | -12.95678 | -46.19138 | 2024-10-11 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a37b2150-943e-3424-82c7-b58d6797d962 | -12.90093 | -41.11779 | 2024-10-11 03:38:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7b3391c5-12a8-3cb7-83c8-0c2309ada53e | -12.78321 | -44.88167 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ab43fa5e-b171-35b3-96c1-cc9113d64d4a | -12.78247 | -44.88536 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7f4e9546-de80-3bc1-a7ce-e2881e8c3800 | -12.78174 | -44.88904 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2e7c26e9-d765-3649-a1b1-b656f639d7f6 | -12.78171 | -44.88528 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ce94148b-8faf-3c98-9566-66baf9b1d289 | -12.781 | -44.88897 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| cc28c77e-2f84-3a6c-a985-f8706d3c7017 | -12.78082 | -38.49798 | 2024-10-11 03:38:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ec790e7b-1382-3039-9037-741091f40c50 | -12.77996 | -44.86963 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 4d2c57c6-2dbf-3a92-a2ad-0f5b281cd914 | -12.77923 | -44.87325 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3d3919ab-3c46-3d55-85c7-fc0959740a3f | -12.77909 | -44.86951 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 8376948c-d6d6-3afa-87bd-231e498e5860 | -12.7785 | -44.87689 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c4f2957b-b30e-31bd-b853-d46f0a6986a7 | -12.77839 | -44.87314 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7c3e0e05-9801-3b18-b3f0-133a62da1c62 | -12.77777 | -44.88054 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f82498fd-ea44-3311-a33f-acfea027cef8 | -12.77769 | -44.87679 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ccc55782-a32c-3509-9247-ed9813362006 | -12.77703 | -44.8842 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a920b7ed-dd24-3127-b0e7-4d649db8bf01 | -12.77698 | -44.88044 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b76abf0b-5287-38fb-b309-78260a912689 | -12.7763 | -44.88787 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a53f60b5-e56e-317e-8f5b-b543d328aa2c | -12.77627 | -44.88411 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2f1e21cc-9e54-300a-a1b7-b2fe812da251 | -12.77556 | -44.88779 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3297eef6-59fb-36de-8dc8-4afa01ea73f2 | -12.77524 | -44.86493 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c6d2fb0f-4479-31a7-88d1-03b73f6382fa | -12.77451 | -44.86854 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| aefdea12-7e8e-347c-9355-74dbdbdc2607 | -12.77434 | -44.86478 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f5405b0e-7bda-3c64-bf71-57ec857a36a9 | -12.77378 | -44.87217 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 510139d8-9769-3f96-8afb-ba8b6ef816f2 | -12.77364 | -44.8684 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 7266a4cb-e934-3a1d-9329-88a7d5666041 | -12.77305 | -44.8758 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b12ea7e3-8901-3df6-9d94-e61aa44c56bc | -12.77294 | -44.87204 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 1f51a83d-9a28-30bc-8a83-f5ca2cde3a5b | -12.77232 | -44.87944 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e649b371-e542-3f10-a06f-ac8487ad3cea | -12.77223 | -44.87568 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| acbb7733-c184-314b-b952-fc8e151fc228 | -12.77159 | -44.88308 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a819e2c5-61e3-38fa-ad46-d556e69523ae | -12.77153 | -44.87933 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| ac39d6ab-3bbe-3d88-b101-9aa880c1ab55 | -12.77085 | -44.88673 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c58b05fe-b55d-379e-8675-4aa44f9853b3 | -12.77082 | -44.88298 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2e00b666-d521-32bd-bdf4-5cfc108a6258 | -12.7682 | -44.86731 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b2ec1304-db15-3c9f-8992-b2264e05d2de | -12.76749 | -44.87094 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b56f6d97-2d86-3cc9-8047-980da66b339e | -12.76678 | -44.87458 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 6737e494-0201-3f53-85e1-6e54963b8f49 | -12.76608 | -44.87821 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |


[Clique aqui para ver as próximas entradas](README33.md)
