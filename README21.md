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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7771ef5c-505f-3731-a32b-e5cbc762293b | -8.79826 | -44.72205 | 2024-10-24 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d1cc778-bcba-376a-9d0e-a0d91199db68 | -8.79768 | -44.72531 | 2024-10-24 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bce1969c-bb3f-3cc5-868c-7a535201b0c8 | -8.79708 | -44.72856 | 2024-10-24 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1b872ee-cc76-35c0-856e-d34d45434a3a | -8.79649 | -44.73182 | 2024-10-24 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12cd6a7b-c59a-3518-8dc1-1fc34d6bda07 | -8.79591 | -44.73507 | 2024-10-24 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d3aba2b-7e6d-38f3-9f66-a531ff1b5ec5 | -8.79532 | -44.73832 | 2024-10-24 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e000cc01-2890-34d3-a8af-b8bb63d86aeb | -8.79473 | -44.74158 | 2024-10-24 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c47ba23e-8901-3f71-ab2e-f00441a6f86b | -8.79414 | -44.74483 | 2024-10-24 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ffa3a65-2f7d-3db6-95a3-2afd98b284cb | -8.78889 | -44.74392 | 2024-10-24 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a31d4a5-3712-32e9-963c-c74d608a9e73 | -15.34421 | -39.87113 | 2024-10-24 03:42:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e59efc5b-15fb-34e7-99c2-6bbd4c756143 | -14.6165 | -40.60285 | 2024-10-24 03:42:00 | NOAA-20 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 86c7b9ff-c438-3db3-9280-41f576290762 | -14.27173 | -44.56205 | 2024-10-24 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d070a10-071e-3202-8505-99a2f7885ad6 | -14.26705 | -44.56104 | 2024-10-24 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce6b8614-9b1c-3e10-8bce-6c7c3b03b3d5 | -14.16295 | -44.17994 | 2024-10-24 03:42:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fb98903-1b7a-3727-9791-8edbd63da13d | -14.02061 | -43.29903 | 2024-10-24 03:42:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1566997e-8e3f-3b1c-9663-71481c3072d6 | -14.01982 | -43.30332 | 2024-10-24 03:42:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 70cfbdf2-7dba-3e1b-9e09-a5798a313695 | -13.73141 | -44.28781 | 2024-10-24 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fc761fcd-95d7-3a12-a08e-a6c208c4ebed | -13.71729 | -42.8926 | 2024-10-24 03:42:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 063c8ed3-9bd8-3939-bbb4-d52bd76d3688 | -13.71651 | -42.89696 | 2024-10-24 03:42:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 242dd1ca-f998-36c4-814e-073353669b7f | -13.70946 | -43.66504 | 2024-10-24 03:42:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e363e6d3-76ab-3c53-8bcf-2341d1bf8b4a | -13.70863 | -43.66961 | 2024-10-24 03:42:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5deed20c-496a-33f3-a835-bd5fa552a4cd | -13.70528 | -42.88613 | 2024-10-24 03:42:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a0042f64-3fd4-324c-8af8-0a217d8eb37f | -13.70206 | -42.92845 | 2024-10-24 03:42:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b5f1466c-7fae-38c1-845d-7b6a2ab4ed64 | -13.70104 | -42.8853 | 2024-10-24 03:42:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| da01a85e-243a-3291-b231-cd032ca0718a | -13.68444 | -43.05101 | 2024-10-24 03:42:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 722a1989-1373-3d0f-93bc-0ccbb87090fd | -13.65734 | -42.49858 | 2024-10-24 03:42:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 699ba07a-2e81-3ef3-946c-9ad128fde4e0 | -13.631 | -43.66368 | 2024-10-24 03:42:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d668fb1-171f-3a5e-91e2-421d92080285 | -13.6297 | -42.53302 | 2024-10-24 03:42:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 34cfded8-7a1d-3ec7-a8bf-72700a2cd752 | -13.55915 | -46.52838 | 2024-10-24 03:42:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f49aa28-bdfb-306f-803b-6318a5053510 | -13.55305 | -46.53085 | 2024-10-24 03:42:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97fec14f-9f08-324a-a3cf-faa0210a0484 | -13.50975 | -44.41367 | 2024-10-24 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2197a6c1-058d-3f2c-9845-7d20399e0b59 | -13.50875 | -44.41901 | 2024-10-24 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ae6d7675-03f4-3621-93a2-31df7c72ad39 | -13.4993 | -44.41732 | 2024-10-24 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77b68f39-50d7-3fa2-8428-0941b7de8761 | -13.47356 | -44.02689 | 2024-10-24 03:42:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36e77118-3ebd-3bfb-a387-d823381d846c | -13.43234 | -44.35178 | 2024-10-24 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 633cfb61-e6a7-3252-9687-ea68aad63a28 | -13.43138 | -44.35695 | 2024-10-24 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8cde3cef-1bb7-38aa-aa1f-d7115d8f004f | -13.35962 | -43.92735 | 2024-10-24 03:42:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89b7d8b1-be66-3f3f-a653-e04aa74cb480 | -13.35871 | -43.93216 | 2024-10-24 03:42:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5161c9aa-947a-32e4-935c-036cdfe61fb4 | -13.35504 | -43.92645 | 2024-10-24 03:42:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| edc1e79e-d2dd-3b4b-b632-e35c70d204b5 | -13.34347 | -43.68195 | 2024-10-24 03:42:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 803fb493-1f2f-36a6-8c2a-ab7932ccd824 | -13.06469 | -39.93392 | 2024-10-24 03:42:00 | NOAA-20 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e8ec1e3f-89b5-3d36-8dfb-a62c480b2094 | -12.95521 | -48.87271 | 2024-10-24 03:42:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4d186c0e-20c1-3e40-9cd9-6e539f0f9688 | -12.95415 | -48.87783 | 2024-10-24 03:42:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a16d509b-db39-3fe4-863d-b1ece4c23d36 | -11.41403 | -40.62374 | 2024-10-24 03:42:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9ce3a5bb-f52a-3999-aa8e-898fa6c25e76 | -12.82104 | -38.41934 | 2024-10-24 03:42:00 | NOAA-20 | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2b3ceaca-7ecd-39c7-a951-4dbd590cb43f | -12.78023 | -38.49735 | 2024-10-24 03:42:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e3fdbb66-40d7-3528-b21c-015278297165 | -12.71105 | -43.85695 | 2024-10-24 03:42:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46a6d0d4-c94f-3c38-ab8c-a5164c11ff07 | -12.69355 | -43.84854 | 2024-10-24 03:42:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c23dd4d0-00ee-37c9-8ce7-049874c6c051 | -12.69127 | -43.84106 | 2024-10-24 03:42:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2ac0b3f0-3ad5-3b34-bfa5-1aa8feb99a34 | -12.69078 | -43.83793 | 2024-10-24 03:42:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 347f15e4-6c19-3d6b-bd91-28296995d69a | -12.69039 | -43.84593 | 2024-10-24 03:42:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 19f70d14-634c-34b1-9968-66db530bddbf | -12.68987 | -43.84279 | 2024-10-24 03:42:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0a973224-93e5-3b07-ac85-553f90752f00 | -12.68951 | -43.85081 | 2024-10-24 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ac238799-42d7-3913-b36c-9ee20dd12b4f | -12.68895 | -43.84766 | 2024-10-24 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 52966a10-6fc1-3ac9-ab90-3a12d6018749 | -12.68667 | -43.84017 | 2024-10-24 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4ff6c1a5-c513-37aa-988e-cdd510901b6c | -12.68579 | -43.84504 | 2024-10-24 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d8c29ad0-2642-3c8b-8835-ff760cf473a1 | -12.68526 | -43.84191 | 2024-10-24 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f5e07363-2013-3ea9-bdab-a9b95ae06768 | -12.6849 | -43.84993 | 2024-10-24 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b24a32c8-4c14-3621-adad-890d5350e72a | -12.68434 | -43.84679 | 2024-10-24 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 867c56b5-1101-310d-a404-05f62d714fba | -12.68342 | -43.85166 | 2024-10-24 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66ffc971-105a-3651-b2e2-75124831ebfe | -12.68118 | -43.84415 | 2024-10-24 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5899ff7b-325a-34af-9465-e66e8f8a1650 | -12.68066 | -43.84102 | 2024-10-24 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 70b9514e-213a-3ec9-b792-5986a25e36c1 | -12.68029 | -43.84904 | 2024-10-24 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e7dee4c2-e942-30be-b391-77feb36051db | -12.67974 | -43.84591 | 2024-10-24 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 03ad7aca-a091-381a-a8ef-f1c037692883 | -12.67881 | -43.85078 | 2024-10-24 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76901aa2-7ff9-34fc-b362-bc595e78c144 | -12.65804 | -43.24306 | 2024-10-24 03:42:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60557105-1b2c-343b-9437-8dd1423ffa38 | -12.59987 | -44.18333 | 2024-10-24 03:42:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d690720-2e62-3e6a-8f01-ad3d5bd02edd | -12.59517 | -44.18232 | 2024-10-24 03:42:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1796da51-c77f-38f6-905b-2547dda3f2ca | -12.48817 | -43.37711 | 2024-10-24 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7bc2eecb-e883-3f6c-86b5-25cfdbb30dac | -12.4488 | -43.74508 | 2024-10-24 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59875fc3-3266-3052-b401-66aab5ebc800 | -12.44791 | -43.74989 | 2024-10-24 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85c07707-d23b-3455-9477-e8bf44031495 | -12.42447 | -43.28223 | 2024-10-24 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f65d6d5d-68d9-30bd-977b-c84ec46283d3 | -12.28517 | -43.83546 | 2024-10-24 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c4d7813-03b4-3a8a-8049-6ccfc7cf4770 | -12.13862 | -43.47907 | 2024-10-24 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7c3f0711-5d27-3f02-9ad5-8e048e7199e2 | -12.13514 | -43.47248 | 2024-10-24 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8fd4193b-5b5b-3233-82af-66a65741037a | -12.13416 | -43.47784 | 2024-10-24 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c9760da2-f157-38fa-8ba0-09d47139ab34 | -11.99332 | -43.91371 | 2024-10-24 03:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6fbe69ae-fe7f-36fa-a537-12fdbeab1ed7 | -11.9517 | -44.16802 | 2024-10-24 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 073d13ab-6eb2-30a0-8676-8544952e257d | -11.94694 | -44.16708 | 2024-10-24 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16439859-54e2-35d8-b292-9bbd97dc5723 | -11.88206 | -44.71336 | 2024-10-24 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb46bfcc-de82-3e35-8928-8fd89317d900 | -11.82514 | -45.17985 | 2024-10-24 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb549694-b241-33f2-949d-106606adceff | -11.77589 | -44.21007 | 2024-10-24 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22450933-065e-3d4e-8af0-b001526ca922 | -11.62762 | -44.96752 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b324bf30-f6f2-34fe-9e21-a2aebd10e3d1 | -11.62705 | -44.97053 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cacabab8-fc01-3146-907f-be67edb7ae72 | -11.62695 | -44.92372 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57e8ca9b-1376-3ccc-9ed5-ffe2c932cbdc | -11.62642 | -44.92661 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 238f1dd6-1740-37ee-a475-bbe28a1a8bf8 | -11.62544 | -44.92414 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c639f870-7136-331d-9f45-120e4d7e8ab8 | -11.62488 | -44.92703 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e5e684e6-a84f-35c3-8ab8-1d8d87005ee6 | -11.62189 | -44.92281 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 69cfba36-7b55-30f7-beb3-b650a61a2bfb | -11.62136 | -44.92572 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d22b16a9-e8aa-3c7b-b401-f78e90ae2a59 | -11.62038 | -44.92325 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce8cc024-aeeb-3a07-aebd-44558c120a63 | -11.61983 | -44.92616 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 09d20c36-b2cb-3829-8036-75732475402d | -11.55967 | -42.18865 | 2024-10-24 03:42:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6e82d16c-c2fc-30c2-b137-f07a7d848f01 | -11.55803 | -44.84589 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8ee0c99-036c-3c83-af30-0191a9cdce28 | -11.55747 | -44.84885 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ede2871b-776f-3f6b-bc9b-92db197d047a | -11.55301 | -44.84492 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2d739e4-8056-3050-9a94-959bf91cef04 | -11.44896 | -37.99007 | 2024-10-24 03:42:00 | NOAA-20 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 74823517-8a29-3b97-8a8d-1c221633c39d | -11.41619 | -40.62592 | 2024-10-24 03:42:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 691bce90-03ef-361a-92bf-9a5ed3a3ddac | -11.3962 | -44.97278 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eea4bb05-fcda-3fc9-bcd8-2cedc6c07de5 | -11.39446 | -44.97013 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README22.md)
