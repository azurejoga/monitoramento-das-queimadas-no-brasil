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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 698932aa-e161-30c2-a96d-d0aa7eee53ee | -15.19229 | -47.94462 | 2024-10-02 03:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f455c7ba-9200-3332-aa30-d2521443b1bc | -15.17628 | -46.24179 | 2024-10-02 03:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96f2b425-95f7-3551-8a43-96a53779166f | -15.16534 | -46.23896 | 2024-10-02 03:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a01adc92-ef7e-3774-a610-a0df2b10a785 | -15.16422 | -46.24408 | 2024-10-02 03:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 473c3c2b-294d-3c6b-8c6c-6a3e1dca8235 | -15.16389 | -46.23785 | 2024-10-02 03:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c7f24d8-e601-3a3a-a129-c142039a9eb1 | -14.8617 | -45.11196 | 2024-10-02 03:32:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26d2e185-ab1a-3ed8-bc14-f4b37297e82b | -14.85578 | -45.11061 | 2024-10-02 03:32:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 462fed66-5a33-32f4-95d5-603b30855fce | -14.82808 | -47.68692 | 2024-10-02 03:32:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| af918a62-90db-35d2-a97e-7ebd8091ba7a | -14.82132 | -47.68478 | 2024-10-02 03:32:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b253a32e-f2fc-32f7-9979-c0fdf2afb25c | -14.65375 | -45.91953 | 2024-10-02 03:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 518bf712-8e49-3d89-8fcc-4478ac49a9cf | -14.64752 | -45.91808 | 2024-10-02 03:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1602dc06-7fdf-3ab1-818b-c960b2f74513 | -14.57165 | -44.83455 | 2024-10-02 03:32:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1477bbc6-b27d-33dd-884a-e787dd7b8ee7 | -14.57073 | -44.83901 | 2024-10-02 03:32:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afc3cd59-c8ce-3957-9470-72ba6823582a | -14.56671 | -44.82878 | 2024-10-02 03:32:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0ea28c6-1a7d-3d27-bf30-c334636b2b2a | -14.5658 | -44.83319 | 2024-10-02 03:32:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 7f2b339c-18b9-32f5-99d8-14334d137f56 | -14.56488 | -44.83762 | 2024-10-02 03:32:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 96d18461-b717-39c2-b0e5-b42f70b5c4ed | -14.56397 | -44.84204 | 2024-10-02 03:32:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c88357c2-f130-3495-a3a4-29dd54d1eed6 | -14.39808 | -43.27502 | 2024-10-02 03:32:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d627da1-651a-367b-97e3-fa08b6c5738d | -14.39741 | -43.27845 | 2024-10-02 03:32:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 152a5c19-63d1-3f86-8857-b8c16d9e07f7 | -14.39527 | -43.27436 | 2024-10-02 03:32:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dcd11b01-2c33-3a40-b613-49f278c4298a | -14.39457 | -43.27779 | 2024-10-02 03:32:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b29335ea-bbbe-31f7-af71-d1259a62173a | -14.39274 | -43.27391 | 2024-10-02 03:32:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e1240ff3-d32d-3c6a-b969-bbd83ecbacf8 | -14.39206 | -43.27736 | 2024-10-02 03:32:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 33744ff5-5051-3836-9b40-3a9a202e4043 | -14.175 | -46.46703 | 2024-10-02 03:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b308071b-8296-3089-aef6-b8a9510b65ba | -14.17389 | -46.47229 | 2024-10-02 03:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf5d8925-3342-3760-9bf8-90ab9db47067 | -14.00816 | -42.1481 | 2024-10-02 03:32:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c94085c2-4841-3467-b7c9-c2bfc8fd52d6 | -23.28897 | -45.29299 | 2024-10-02 03:34:00 | NPP-375D | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 67dd5a2c-de5b-3b42-ac85-0dfcc3ad4d66 | -23.28827 | -45.29623 | 2024-10-02 03:34:00 | NPP-375D | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 85c7a54b-632d-3f67-9ef9-de8746deb4f5 | -23.06857 | -45.90695 | 2024-10-02 03:34:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 94f1d161-6378-3d0e-8947-f6f219442812 | -23.06778 | -45.91053 | 2024-10-02 03:34:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d72614e2-7464-32a5-9e3f-513f0e93e673 | -23.06547 | -45.90481 | 2024-10-02 03:34:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fb0c821e-9276-3b3b-aaa0-8bd8e7498df4 | -23.06468 | -45.90831 | 2024-10-02 03:34:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 817f177e-0e58-34d5-9f04-d03c97ccad04 | -22.9073 | -45.10362 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ac7e5060-b314-3362-8cff-b56f57933f6c | -22.90555 | -45.1009 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 43ee5d97-8b0f-30f7-a9c0-e3d5a0ea2d6f | -22.90479 | -45.11489 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f97edc74-3039-3017-b8f0-ecad0f7e0025 | -22.90474 | -45.10472 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| f4c4d028-d2a5-36e0-b6d2-f7aff7592307 | -22.90307 | -45.09854 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 34931124-482d-3ad9-a739-baaec693c22a | -22.90306 | -45.11257 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d05d367b-728e-3549-8925-b17f1e2ef187 | -22.90228 | -45.1162 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9e808a9c-9bf3-3d4a-8322-f4b854c5caf3 | -22.9022 | -45.10247 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 0c046207-32a7-3fdd-b220-882ee439f68e | -22.90131 | -45.10647 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a68e0e62-d040-3e13-9c7e-1384250d483c | -22.90126 | -45.09602 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| b5563409-fb93-35c1-8684-a8bf8a3bb6fe | -22.90044 | -45.09983 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 340a6709-080a-38f8-9490-8ceb5e3019e4 | -22.89957 | -45.10392 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 92b0204c-c59e-3876-9963-8dffbe3fd8f5 | -22.89796 | -45.12152 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 96dd5317-a2c6-3aeb-bc49-a573b80e4cb7 | -22.8963 | -45.11917 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3df9905d-960d-3486-b940-5f80d7bf9180 | -22.89614 | -45.09498 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 34fea386-d412-3ee4-88fa-d7bef049b140 | -22.89549 | -45.12295 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d24cc8f3-e239-3189-a01f-c36588255abe | -22.89529 | -45.09892 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5e94f8bc-2efd-3f0d-8058-3bd7aa526165 | -22.89439 | -45.10316 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 67fec485-d5af-36cf-85b3-d49e31a3ed88 | -22.89353 | -45.10715 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d0645663-0e8c-33cd-8714-67f0755449ab | -22.8917 | -45.09077 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 15268a08-0126-3cb4-8b3f-65fa2702c584 | -22.89091 | -45.09446 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 144c4111-22e5-3b5a-ac5e-6c9e70fcb371 | -22.89007 | -45.09836 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4fcb2df4-6ebe-3709-8682-ee183c91fea6 | -22.88922 | -45.10234 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 89b58847-25d6-3082-8118-fc41bf733de1 | -22.88837 | -45.10628 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3b7d30fb-178e-3e27-be72-2f405250ff79 | -22.88667 | -45.11418 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 19ac2ca8-64f6-31b3-81c2-4d94f2cb31f4 | -22.88654 | -45.08997 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bbf84bad-ebc7-3726-9cc8-da6d7dfa68e8 | -22.88231 | -45.10958 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 64f8eb51-0737-3ede-a3c9-48092e0e36a9 | -22.88149 | -45.1134 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ddb54e1e-4dac-309c-ba35-9d236d85807b | -22.88136 | -45.08921 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e87afcd4-d94b-3d11-9416-025ca6e3344e | -22.78756 | -45.19476 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c8f546c3-3f8c-3e59-9414-34847e2fe4c5 | -22.78344 | -45.193 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fba2f7ec-9539-3b10-b4f6-2247008af2ef | -22.78274 | -45.19616 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 49f1e4c9-c4b2-38c5-8f41-82c789593688 | -22.78245 | -45.19345 | 2024-10-02 03:34:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b1693e91-29f1-35c2-bf05-0e7efa44fe44 | -22.77153 | -44.65935 | 2024-10-02 03:34:00 | NPP-375D | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| cf62e102-4817-302a-9fbb-30a9469f1ec2 | -22.77107 | -44.66011 | 2024-10-02 03:34:00 | NPP-375D | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 89ade9e7-3092-39fb-920c-f6ae41d53f95 | -22.76884 | -44.64752 | 2024-10-02 03:34:00 | NPP-375D | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d522870f-6caf-353b-9541-bb88beccce77 | -22.76774 | -44.65268 | 2024-10-02 03:34:00 | NPP-375D | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 50d8487f-a5f3-3878-aee3-df0b532632dc | -22.76655 | -44.65829 | 2024-10-02 03:34:00 | NPP-375D | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 681989c9-d62c-342e-9234-bef075894653 | -22.76395 | -44.64606 | 2024-10-02 03:34:00 | NPP-375D | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 410cedbc-0860-3b19-9a02-466509f5f25e | -22.76281 | -44.65138 | 2024-10-02 03:34:00 | NPP-375D | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c7e54d10-9ca3-39ed-967a-80bdabeaeecc | -23.16591 | -49.60289 | 2024-10-02 03:34:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 7eab52db-6372-39b5-9f7a-34969a21c2c9 | -25.82564 | -50.25485 | 2024-10-02 03:34:00 | NPP-375D | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 44fc0d03-8636-33c2-83b7-e1795b84ec17 | -25.82418 | -50.26056 | 2024-10-02 03:34:00 | NPP-375D | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d8367938-3f6f-3f06-8f06-905f776c506d | -25.03341 | -50.71775 | 2024-10-02 03:34:00 | NPP-375D | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c05f4b2c-4502-3f2d-ba8f-d102abaa66c9 | -25.03173 | -50.72408 | 2024-10-02 03:34:00 | NPP-375D | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4baba98a-7a4d-3209-9654-21a2b3c0054f | -25.03131 | -50.71693 | 2024-10-02 03:34:00 | NPP-375D | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 24fba2d5-8a6a-374c-9b6d-726a8c2918f0 | -25.02964 | -50.72336 | 2024-10-02 03:34:00 | NPP-375D | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 5989b3c7-ebf6-3e43-a3f8-f8f92fe15f0e | -25.02682 | -50.71566 | 2024-10-02 03:34:00 | NPP-375D | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a3308ba6-344e-36fc-95b7-34ef63894517 | -25.02505 | -50.7223 | 2024-10-02 03:34:00 | NPP-375D | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| caef9656-e0e7-3b1a-abb4-83e97977bd36 | -23.81652 | -47.64619 | 2024-10-02 03:34:00 | NPP-375D | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ab02a903-de51-3df5-a7b7-ef7e9a8a300a | -23.81544 | -47.65079 | 2024-10-02 03:34:00 | NPP-375D | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76793e61-df36-3740-9a17-c52fc4942649 | -23.51615 | -46.26944 | 2024-10-02 03:34:00 | NPP-375D | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 154bc4a5-ad2f-37b3-908b-327da2a10699 | -23.51449 | -51.09781 | 2024-10-02 03:34:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 7daddc55-a8af-3669-b3f9-7cb094722018 | -23.51261 | -51.10484 | 2024-10-02 03:34:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 776ad889-4663-3686-a7f3-b16dac55007c | -23.51083 | -46.26781 | 2024-10-02 03:34:00 | NPP-375D | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8f86b296-2c3b-3f00-a0f7-fb70db32f46a | -23.51082 | -47.22404 | 2024-10-02 03:34:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 261838ff-f216-3c05-8e67-00021d18e74b | -23.51081 | -51.09906 | 2024-10-02 03:34:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 86f93650-1284-3fd9-9fbe-ba32087e17b7 | -23.50972 | -47.22868 | 2024-10-02 03:34:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 42cc006d-ffd5-3882-af2d-c97a21e9d091 | -23.50957 | -47.22588 | 2024-10-02 03:34:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 99d3e60d-4137-3f6a-9aaf-31af1d62e616 | -23.50894 | -51.10622 | 2024-10-02 03:34:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8600cdfc-190c-3db9-9a14-7e83f695d9c4 | -23.50866 | -47.23316 | 2024-10-02 03:34:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| fbd23ace-13a3-3435-9c22-ce37ac219d8a | -23.50852 | -47.23045 | 2024-10-02 03:34:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 32b99f6e-d477-36c7-abbf-d7e8539a0bfb | -23.50513 | -47.22264 | 2024-10-02 03:34:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e95fab73-4f90-37e4-a4e8-bcb3a5733cbd | -23.50406 | -47.2271 | 2024-10-02 03:34:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9471b243-1e17-3361-8fc1-335746c9e84b | -23.5039 | -47.22438 | 2024-10-02 03:34:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f86ad7c6-d1df-3c9a-b46f-a9fdc6655a72 | -23.50287 | -47.22882 | 2024-10-02 03:34:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b0a6cfc8-ad47-31ed-b9c6-ccdbaec74a8e | -23.35721 | -47.02293 | 2024-10-02 03:34:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 48520c7b-048e-31c3-b700-1ef99d5b3523 | -23.35381 | -47.01691 | 2024-10-02 03:34:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |


[Clique aqui para ver as próximas entradas](README56.md)
